import { Component } from '@angular/core';
import { AudioRecorderService } from '../../services/audio-recorder.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
import { RecordedAudioOutput } from '../../models/recorded-audio-output.model';
import { blob } from 'stream/consumers';

@Component({
  selector: 'app-voice-recorder',
  imports: [],
  templateUrl: './voice-recorder.component.html',
  styleUrl: './voice-recorder.component.css'
})
export class VoiceRecorderComponent {
  isRecording = false;
  recordedTime = '00:00';
  blobUrl!: SafeUrl;
  recordedAudio!: RecordedAudioOutput;

  constructor(private audioRecordingService: AudioRecorderService,
private sanitizer: DomSanitizer) { 
  this.audioRecordingService.getRecordingFailed().subscribe(() => {
    this.isRecording = false;
  });

}

  startRecording() {
    this.isRecording = true;
    this.audioRecordingService.startRecording();
    this.audioRecordingService.getRecordedTime().subscribe((time) => {
      this.recordedTime = time;
    });
  }

  stopRecording() {
    this.isRecording = false;
    this.audioRecordingService.stopRecording();
    this.audioRecordingService.getRecorded().subscribe(event => {
      this.recordedAudio = event;
    });
    this.blobUrl = this.sanitizer.bypassSecurityTrustUrl(URL.createObjectURL(this.recordedAudio.blob));
  }

  clearRecording() {
    this.blobUrl = ''; 
    this.recordedTime = '00:00';
    this.isRecording = false;
  }

  downloadRecording() {
    const url = window.URL.createObjectURL(this.recordedAudio.blob);
    const link =document.createElement('a');
    link.href = url;
    link.download = this.recordedAudio.title + '.webm';
    link.click();
  }

}
