import { Component } from "@angular/core"
import { PreferenceService } from "../../services/preference/preference.service"
import { WaveformComponent } from "../waveform/waveform.component"
import { AudioService } from "../../services/audio/audio.service"

@Component({
  selector: "app-voice",
  standalone: true,
  imports: [WaveformComponent],
  templateUrl: "./voice.component.html",
  styleUrl: "./voice.component.css",
})
export class VoiceComponent {
  constructor(private preference: PreferenceService) {}
}
