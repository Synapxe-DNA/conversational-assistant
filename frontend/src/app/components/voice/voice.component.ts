import { Component } from "@angular/core";
import { PreferenceService } from "../../services/preference/preference.service";
import { WaveformComponent } from "../waveform/waveform.component";
import { AudioService } from "../../services/audio/audio.service";
import { MicrophoneButtonComponent } from "../microphone-button/microphone-button.component";
import { MicState } from "../../types/mic-state.type";
import { SecondaryButtonComponent } from "../secondary-button/secondary-button.component";

@Component({
  selector: "app-voice",
  standalone: true,
  imports: [
    WaveformComponent,
    MicrophoneButtonComponent,
    SecondaryButtonComponent,
  ],
  templateUrl: "./voice.component.html",
  styleUrl: "./voice.component.css",
})
export class VoiceComponent {
  micState: MicState = MicState.PENDING;

  constructor(private preference: PreferenceService) {}
}
