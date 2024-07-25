import { Component, EventEmitter, Input, Output } from "@angular/core";
import { CommonModule } from "@angular/common";
import { LucideAngularModule } from "lucide-angular";

export enum MicState {
  PENDING = "pending",
  ACTIVE = "active",
  DISABLED = "disabled",
}

@Component({
  selector: "app-microphone-button",
  standalone: true,
  imports: [CommonModule, LucideAngularModule],
  templateUrl: "./microphone-button.component.html",
  styleUrl: "./microphone-button.component.css",
})
export class MicrophoneButtonComponent {
  MicState = MicState;
  @Input() state: MicState = MicState.PENDING;
  @Output() stateChange = new EventEmitter<MicState>();

  get buttonClass() {
    switch (this.state) {
      case MicState.PENDING:
        return "tw-bg-yellow-500";
      case MicState.ACTIVE:
        return "tw-bg-green-500";
      case MicState.DISABLED:
        return "tw-bg-gray-500 tw-cursor-not-allowed";
      default:
        return "tw-bg-blue-500";
    }
  }

  onClick() {
    if (this.state !== MicState.DISABLED) {
      this.state =
        this.state === MicState.PENDING ? MicState.ACTIVE : MicState.PENDING;
      this.stateChange.emit(this.state);
    }
  }
}
