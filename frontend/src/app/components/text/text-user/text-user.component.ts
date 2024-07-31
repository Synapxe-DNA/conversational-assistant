import { Component, Input } from "@angular/core";
import { CommonModule } from "@angular/common";
import { Message } from "../../../types/message.type";

@Component({
  selector: "app-text-user",
  standalone: true,
  imports: [CommonModule],
  templateUrl: "./text-user.component.html",
  styleUrl: "./text-user.component.css",
})
export class TextUserComponent {
  @Input() message: Message | null = null;

  get messageText(): string {
    return this.message?.message || "";
  }
}
