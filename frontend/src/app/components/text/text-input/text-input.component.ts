import { Component, Input, ViewChild, ElementRef } from '@angular/core';
import { Message, MessageSource, MessageRole } from '../../../types/message.type';
import { LucideAngularModule } from 'lucide-angular';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

const sources: MessageSource[] = [
  {
    title: "When is Your Baby Due?",
    description: "When is Your Baby Due?",
    url: "https://www.healthhub.sg/live-healthy/when-is-your-baby-due",
    cover_image_url: "https://ch-api.healthhub.sg/api/public/content/8692c864101e4603868fb170c00230fe?v=534ae16e&t=livehealthyheaderimage",
  },
  {
    title: "Important Nutrients: What Should You Eat More Of?",
    description: "Important Nutrients: What Should You Eat More Of? Important Nutrients: What Should You Eat More Of? Important Nutrients: What Should You Eat More Of?",
    url: "https://www.healthhub.sg/live-healthy/important-nutrients-what-should-you-eat-more-of",
    cover_image_url: "https://ch-api.healthhub.sg/api/public/content/3885d0458c0a4521beb14ca352730423?v=646204cc&t=livehealthyheaderimage",
  }
];

@Component({
  selector: 'app-text-input',
  standalone: true,
  imports: [LucideAngularModule, FormsModule, CommonModule],
  templateUrl: './text-input.component.html',
  styleUrl: './text-input.component.css'
})
export class TextInputComponent {
  @Input() messages: Message[] = [];
  newMessage: string = "";
  @ViewChild("chatWindow") chatWindow!: ElementRef;
  waitingForBotResponse: boolean = false;

  sendMessage() {
    if (this.newMessage.trim()) {
      this.messages.push({
        id: "1",
        profile_id: "1",
        role: MessageRole.User,
        message: "This is a user message.",
        timestamp: "2023-08-01T12:00:00Z",
        sources: [],
      });
      this.newMessage = "";
      this.scrollToBottom();
      this.waitingForBotResponse = true;

      setTimeout(() => {
        this.messages.push({
          id: "2",
          profile_id: "1",
          role: MessageRole.System,
          message: "This is a system message.",
          timestamp: "2023-08-01T12:00:00Z",
          sources: sources,
        });
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
