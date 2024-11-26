import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { RecordedAudioOutput } from '../models/recorded-audio-output.model';

@Injectable({
  providedIn: 'root'
})
export class AudioRecorderService {
  private recorder!: MediaRecorder;
  private stream!: MediaStream;
  private startTime!: Date;
  private interval: any;
  private _recorded: Subject<RecordedAudioOutput> = new Subject<RecordedAudioOutput>();
  private _recordingTime = new Subject<string>();
  private _recordingFailed = new Subject<string>();

  getRecorded(): Observable<RecordedAudioOutput> {
    return this._recorded.asObservable();
  }

  getRecordedTime(): Observable<string> {
    return this._recordingTime.asObservable();
  }

  getRecordingFailed(): Observable<string> {
    return this._recordingFailed.asObservable();
  }

  startRecording() {
    if (this.recorder) {
      return;
    }
    let chunks : Blob[] = [];

    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        this.stream = stream;
        this.recorder = new MediaRecorder(this.stream, { mimeType: 'audio/webm' });
        this.recorder.ondataavailable = (event: BlobEvent) => {
          chunks.push(event.data);
        }

        this.recorder.onstop = () => {
            this._recorded.next({ blob: new Blob(chunks, {type : 'audio/webm'}), duration: new Date().getTime() - this.startTime.getTime(), title: 'audio.webm' });
        }
        this.recorder.start();
        this.startTime = new Date();
        this.interval = setInterval(() => {
          const currentTime = new Date();
          const diffTime = currentTime.getTime() - this.startTime.getTime();
          const minutes = Math.floor(diffTime / 60000);
          const seconds = Math.floor((diffTime % 60000) / 1000);
          const time = this.toString(minutes) + ':' + this.toString(seconds);
          this._recordingTime.next(time);
        }, 1000);
      })
      .catch(() => {
        this._recordingFailed.next('Error recording');
      });
  }

  stopRecording() {
    if (this.recorder ) {
      this.recorder.stop();
      clearInterval(this.interval);
    }
  }

  abortRecording() {
    this.stopRecording();
  }

  private toString(value: number): string {
    return value < 10 ? '0' + value : value.toString();
  }
}