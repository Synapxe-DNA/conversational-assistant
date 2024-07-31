import { Component, ElementRef, ViewChild } from "@angular/core";
import { CommonModule } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { LucideAngularModule } from "lucide-angular";
import { TextUserComponent } from "./text-user/text-user.component";
import { Message, MessageRole } from "../../types/message.type";
import { Router } from "@angular/router";

@Component({
  selector: "app-text",
  standalone: true,
  imports: [CommonModule, FormsModule, LucideAngularModule, TextUserComponent],
  templateUrl: "./text.component.html",
  styleUrls: ["./text.component.css"],
})
export class TextComponent {
  messages: Message[] = [];
  newMessage: string = "";
  @ViewChild("chatWindow") chatWindow!: ElementRef;
  waitingForBotResponse: boolean = false;
  private router: Router = new Router();
  profile_id: string = "";

  ngOnInit() {
    const currentPath = this.router.url.split("/");
    this.profile_id = currentPath[2];
  }

  getNextMessageId(): string {
    return this.messages.length == 0
      ? "1"
      : (this.messages.length + 1).toString();
  }

  sendMessage() {
    if (this.newMessage.trim() && !this.waitingForBotResponse) {
      const userMessage: Message = {
        id: this.getNextMessageId(),
        profile_id: this.profile_id,
        role: MessageRole.User,
        message: this.newMessage,
        timestamp: new Date().toISOString(),
      };
      this.messages.push(userMessage);
      this.newMessage = "";
      this.scrollToBottom();
      this.waitingForBotResponse = true;

      setTimeout(() => {
        const botMessage: Message = {
          id: Date.now().toString(),
          profile_id: this.profile_id,
          role: MessageRole.System,
          message: "This is a bot response.",
          timestamp: new Date().toISOString(),
        };
        this.messages.push(botMessage);
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
