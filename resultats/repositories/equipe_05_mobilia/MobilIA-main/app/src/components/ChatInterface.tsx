import React, { useState, useCallback, useRef, useEffect } from "react";
import { ChatMessage } from "./ChatMessage";
import { ChatInput } from "./ChatInput";
import { useRealtime } from "../hooks/realtime";
import { Journey } from "../api/directions";

interface Message {
  id: number;
  text: string;
  isBot: boolean;
  journeys?: Journey[];
}

export function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      text: "Bonjour ! Je suis Mobil-IA, votre assistant pour faciliter vos déplacements. Comment puis-je vous aider aujourd'hui ?",
      isBot: true,
    },
  ]);
  const chatContainerRef = useRef<HTMLDivElement>(null);

  const handleRealtimeUpdate = (message: string, isBot: boolean) => {
    console.log(`Realtime update: ${isBot ? "Bot" : "User"} - ${message}`);
  };
  const onNewMessage = useCallback(
    (text: string, isBot: boolean, journeys?: Journey[]) => {
      console.log(
        `New message received: ${text} (${isBot ? "Bot" : "User"}) : `,
        journeys
      );
      if (journeys && journeys.length > 0) {
        setMessages((prevMessages) => [
          ...prevMessages,
          {
            id: Date.now(),
            text,
            isBot,
            journeys // Corrected from 'journey' to 'journeys'
          }
        ]);
        // setMessages((prevMessages) => [
        //   ...prevMessages,
        //   ...journeys.map((journey) => ({
        //     id: Date.now(),
        //     text,
        //     isBot,
        //     journey,
        //   })),
        // ]);
      } else {
        setMessages((prevMessages) => [
          ...prevMessages,
          { id: Date.now(), text, isBot },
        ]);
      }
    },
    []
  );

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [messages]);

  const { isAudioOn, startAudio, stopAudio } = useRealtime(onNewMessage);

  const handleSendMessage = (text: string) => {
    onNewMessage(text, false);
    // Start audio if it's not already on
    if (!isAudioOn) {
      startAudio();
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden">
      <div
       ref={chatContainerRef}
        className="h-[calc(100vh-16rem)] overflow-y-auto p-4 space-y-4"
        role="log"
        aria-label="Conversation"
      >
        {messages.map((message) => (
          <ChatMessage
            key={message.id}
            message={message.text}
            isBot={message.isBot}
            journeys={message.journeys}
          />
        ))}
      </div>
      <ChatInput
        handleRealtimeUpdate={handleRealtimeUpdate}
        onNewMessage={onNewMessage}
        onSendMessage={handleSendMessage}
      />
    </div>
  );
}
