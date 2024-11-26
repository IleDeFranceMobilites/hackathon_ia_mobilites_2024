import React, { useState } from "react";
import { Send, Mic } from "lucide-react";
import { useRealtime } from "../hooks/realtime";
import { Journey } from "../api/directions";

interface ChatInputProps {
  onNewMessage: (text: string, isBot: boolean, journeys?: Journey[]) => void;
  onSendMessage: (message: string) => void;
  handleRealtimeUpdate: (message: string, isBot: boolean) => void;
}

export function ChatInput({ onSendMessage, onNewMessage }: ChatInputProps) {
  const [message, setMessage] = useState("");
  const { isAudioOn, startAudio, stopAudio } = useRealtime(onNewMessage);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim()) {
      onSendMessage(message);
      setMessage("");
    }
  };

  const handleAudioToggle = () => {
    if (isAudioOn) {
      stopAudio();
    } else {
      startAudio();
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="p-4 border-t border-gray-200 bg-white"
    >
      <div className="flex gap-2">
        <button
          type="button"
          aria-label={
            isAudioOn
              ? "Désactiver la reconnaissance vocale"
              : "Activer la reconnaissance vocale"
          }
          className={`p-2 ${
            isAudioOn
              ? "text-red-600 bg-red-50"
              : "text-blue-600 hover:bg-blue-50"
          } rounded-full transition-colors`}
          onClick={handleAudioToggle}
        >
          <Mic className={`h-6 w-6 ${isAudioOn ? "animate-pulse" : ""}`} />
        </button>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Tapez votre message..."
          aria-label="Message"
          className="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        />
        <button
          type="submit"
          aria-label="Envoyer le message"
          disabled={!message.trim()}
          className="p-2 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <Send className="h-6 w-6" />
        </button>
      </div>
    </form>
  );
}
