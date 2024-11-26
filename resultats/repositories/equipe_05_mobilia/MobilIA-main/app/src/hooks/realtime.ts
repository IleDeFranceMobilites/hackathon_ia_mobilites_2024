import { useState, useEffect, useCallback } from 'react';
import { Player } from '../lib/player';
import { Recorder } from '../lib/recorder';
import { getCurrentLocation } from '../utils/geolocation';
import { Journey } from '../api/directions';

const BUFFER_SIZE = 4096;

export const useRealtime = (onNewMessage?: (message: string, isBot: boolean, journeys?: Journey[]) => void) => {
    const [isAudioOn, setIsAudioOn] = useState(false);
    const [audioPlayer] = useState(() => new Player());
    const [audioRecorder, setAudioRecorder] = useState<Recorder | null>(null);
    const [webSocket, setWebSocket] = useState<WebSocket | null>(null);

    const [currentLocation, setCurrentLocation] = useState<{ latitude: number; longitude: number } | null>(null);

    // useEffect(() => {
    //     let intervalId: NodeJS.Timeout;

    //     const sendLocation = async () => {
    //         try {
    //             const { latitude, longitude } = await getCurrentLocation();
    //             setCurrentLocation({ latitude, longitude });

    //             if (webSocket && webSocket.readyState === WebSocket.OPEN) {
    //                 webSocket.send(JSON.stringify({
    //                     type: 'location_update',
    //                     latitude,
    //                     longitude
    //                 }));
    //             }
    //         } catch (error) {
    //             console.error('Error getting or sending location:', error);
    //         }
    //     };

    //     if (isAudioOn) {
    //         sendLocation(); // Send immediately when audio starts
    //         intervalId = setInterval(sendLocation, 30000); // Then every 30 seconds
    //     }

    //     return () => {
    //         if (intervalId) {
    //             clearInterval(intervalId);
    //         }
    //     };
    // }, [isAudioOn, webSocket]);

    const startAudio = useCallback(async () => {
        try {
            const ws = new WebSocket("ws://localhost:8000/ws");
            setWebSocket(ws);

            await audioPlayer.init(24000);

            let buffer = new Uint8Array();

            const appendToBuffer = (newData: Uint8Array) => {
                const newBuffer = new Uint8Array(buffer.length + newData.length);
                newBuffer.set(buffer);
                newBuffer.set(newData, buffer.length);
                buffer = newBuffer;
            };

            const handleAudioData = (data: ArrayBuffer) => {
                const uint8Array = new Uint8Array(data);
                appendToBuffer(uint8Array);

                if (buffer.length >= BUFFER_SIZE) {
                    const toSend = new Uint8Array(buffer.slice(0, BUFFER_SIZE));
                    buffer = new Uint8Array(buffer.slice(BUFFER_SIZE));

                    const regularArray = String.fromCharCode(...toSend);
                    const base64 = btoa(regularArray);

                    ws.send(JSON.stringify({ type: 'input_audio_buffer.append', audio: base64 }));
                }
            };

            const recorder = new Recorder(handleAudioData);
            setAudioRecorder(recorder);

            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            await recorder.start(stream);

            setIsAudioOn(true);
        } catch (error) {
            console.error('Error starting audio:', error);
            alert('Error accessing the microphone. Please check your settings and try again.');
        }
    }, [audioPlayer]);

    const stopAudio = useCallback(() => {
        if (audioRecorder) {
            audioRecorder.stop();
        }
        if (webSocket) {
            webSocket.close();
        }
        setIsAudioOn(false);
    }, [audioRecorder, webSocket]);

    useEffect(() => {
        if (webSocket) {
            webSocket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                const handleTranscription = (transcript: string, isAIResponse: boolean) => {
                    console.log(`${isAIResponse ? 'AI' : 'User'} transcription:`, transcript);
                    if (typeof onNewMessage === 'function') {
                        onNewMessage?.(transcript, isAIResponse);
                    } else {
                        // console.error('onNewMessage is not a function', onNewMessage);
                    }
                };

                if (data?.type === 'conversation.item.input_audio_transcription.completed') {
                    handleTranscription(data.transcript, false);
                } else if (data?.type === 'response.audio_transcript.done') {
                    handleTranscription(data.transcript, true);
                }
                if (data?.type === 'response.function_call_arguments.done') {
                    console.log('AI function_call_arguments:', data.transcript);
                }
                if (data?.type === 'tools.tool_outputs') {
                    console.log('Received tool output:', data);
                    const args = JSON.parse(data.response.item.args);
                    const output = JSON.parse(data.response.item.output);
                    console.log('tools.tool_outputs:', output);
                    if (args.start && output.length > 0) {
                        onNewMessage?.("Voici les résultats : ", true, output);
                    }

                }
                if (data?.type !== 'response.audio.delta') return;

                const binary = atob(data.delta);
                const bytes = Uint8Array.from(binary, c => c.charCodeAt(0));
                const pcmData = new Int16Array(bytes.buffer);

                audioPlayer.play(pcmData);
            };
        }
    }, [webSocket, audioPlayer, onNewMessage]);

    return {
        isAudioOn,
        startAudio,
        stopAudio
    };
}