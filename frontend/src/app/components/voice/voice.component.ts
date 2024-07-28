import {Component, OnInit} from "@angular/core";
import { PreferenceService } from "../../services/preference/preference.service";
import { WaveformComponent } from "../waveform/waveform.component";
import { AudioService } from "../../services/audio/audio.service";
import { MicrophoneButtonComponent } from "../microphone-button/microphone-button.component";
import { MicState } from "../../types/mic-state.type";
import { SecondaryButtonComponent } from "../secondary-button/secondary-button.component";
import {LucideAngularModule} from "lucide-angular";
import {Button} from "primeng/button";
import {OverlayPanelModule} from "primeng/overlaypanel";
import {InputSwitchChangeEvent, InputSwitchModule} from "primeng/inputswitch";
import {ChatMode} from "../../types/chat-mode.type";
import {FormsModule} from "@angular/forms";

@Component({
  selector: "app-voice",
  standalone: true,
  imports: [
    WaveformComponent,
    MicrophoneButtonComponent,
    SecondaryButtonComponent,
    LucideAngularModule,
    Button,
    OverlayPanelModule,
    InputSwitchModule,
    FormsModule,
  ],
  templateUrl: "./voice.component.html",
  styleUrl: "./voice.component.css",
})
export class VoiceComponent implements OnInit{
  micState: MicState = MicState.PENDING;

  voiceInterrupt:boolean = false
  voiceDetectStart:boolean = false
  voiceDetectEnd:boolean = false

  constructor(private preference: PreferenceService) {
  }

  ngOnInit() {
    this.preference.$voiceDetectInterrupt.subscribe(v => {this.voiceInterrupt = v})
    this.preference.$voiceDetectStart.subscribe(v => this.voiceDetectStart=v)
    this.preference.$voiceDetectEnd.subscribe(v => this.voiceDetectEnd=v)
  }

  prefChatModeToText():void{
    this.preference.setChatMode(ChatMode.Text)
  }

  prefVoiceInterrupt(e:InputSwitchChangeEvent){
    this.preference.setVoiceDetectInterrupt(e.checked)
  }

  prefVoiceStart(e:InputSwitchChangeEvent){
    this.preference.setVoiceDetectStart(e.checked)
  }

  prefVoiceEnd(e:InputSwitchChangeEvent){
    this.preference.setVoiceDetectEnd(e.checked)
  }
}
