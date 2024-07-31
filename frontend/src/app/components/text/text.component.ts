import { Component, ElementRef, ViewChild } from "@angular/core";
import { CommonModule } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { LucideAngularModule } from "lucide-angular";
import { SourceTileComponent } from "../source-tile/source-tile.component";

interface Message {
  text: string;
  type: "user" | "bot";
}
@Component({
  selector: "app-text",
  standalone: true,
  imports: [CommonModule, FormsModule, LucideAngularModule, SourceTileComponent],
  templateUrl: "./text.component.html",
  styleUrls: ["./text.component.css"],
})

export class TextComponent {
  messages: Message[] = [];
  newMessage: string = "";
  @ViewChild("chatWindow") chatWindow!: ElementRef;
  waitingForBotResponse: boolean = false;

  sendMessage() {
    if (this.newMessage.trim()) {
      this.messages.push({ text: this.newMessage, type: "user" });
      this.newMessage = "";
      this.scrollToBottom();
      this.waitingForBotResponse = true;

      setTimeout(() => {
        this.messages.push({ text: "This is a bot response.", type: "bot" });
        this.scrollToBottom();
        this.waitingForBotResponse = false;
      }, 1000);
    }
  }

  scrollToBottom() {
    try {
      this.chatWindow.nativeElement.scrollTop =
        this.chatWindow.nativeElement.scrollHeight;
    } catch (err) {}
  }
}
