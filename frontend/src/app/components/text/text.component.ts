import { Component, ElementRef, ViewChild } from "@angular/core";
import { CommonModule } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { LucideAngularModule } from "lucide-angular";

interface Message {
  text: string;
  type: "user" | "bot";
}

@Component({
  selector: "app-text",
  standalone: true,
  imports: [CommonModule, FormsModule, LucideAngularModule],
  templateUrl: "./text.component.html",
  styleUrls: ["./text.component.css"],
})
export class TextComponent {
  messages: Message[] = [];
  newMessage: string = "";
  @ViewChild("chatWindow") chatWindow!: ElementRef;

  sendMessage() {
    if (this.newMessage.trim()) {
      this.messages.push({ text: this.newMessage, type: "user" });
      this.newMessage = "";
      this.scrollToBottom();

      setTimeout(() => {
        this.messages.push({ text: "This is a bot response.", type: "bot" });
        this.scrollToBottom();
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
