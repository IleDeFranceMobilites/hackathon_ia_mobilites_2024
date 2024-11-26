import { Component } from '@angular/core';
import { VoiceRecorderComponent } from "../voice-recorder/voice-recorder.component";

@Component({
  selector: 'app-chat',
  imports: [VoiceRecorderComponent],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})
export class ChatComponent {

}
