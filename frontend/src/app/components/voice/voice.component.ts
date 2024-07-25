import { Component } from "@angular/core";
import { PreferenceService } from "../../services/preference/preference.service";
import { WaveformComponent } from "../waveform/waveform.component";
import { AudioService } from "../../services/audio/audio.service";
import {
  MicrophoneButtonComponent,
  MicState,
} from "../microphone-button/microphone-button.component";

@Component({
  selector: "app-voice",
  standalone: true,
  imports: [WaveformComponent, MicrophoneButtonComponent],
  templateUrl: "./voice.component.html",
  styleUrl: "./voice.component.css",
})
export class VoiceComponent {
  micState: MicState = MicState.PENDING;

  onMicStateChange(newState: MicState) {
    this.micState = newState;
  }

  onButtonClick(buttonName: string) {
    console.log(`${buttonName} clicked!`);
  }

  constructor(private preference: PreferenceService) {}
}
