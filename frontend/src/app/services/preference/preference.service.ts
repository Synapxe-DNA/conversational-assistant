import { Injectable } from "@angular/core"
import { BehaviorSubject } from "rxjs"
import { ChatMode } from "../../types/chat-mode.type"

@Injectable({
  providedIn: "root",
})
export class PreferenceService {
  /**
   * This service is used to set the user preference across the website.
   */

  $chatMode = new BehaviorSubject<ChatMode>(ChatMode.Voice)
}
