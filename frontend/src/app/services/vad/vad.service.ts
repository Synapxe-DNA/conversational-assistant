import {Injectable} from '@angular/core';
import {continuous, final, skipUntilSaid, SpeechRecognitionService} from "@ng-web-apis/speech";
import {BehaviorSubject, Observable, repeat, retry} from "rxjs";
import {VoiceActivity} from "../../types/voice-activity.type";

@Injectable({
  providedIn: 'root'
})
export class VadService {
  private endTimeout: number = 0

  constructor(
    private recognition: SpeechRecognitionService
  ) {

  }

  start():Observable<VoiceActivity>{

    const vadState = new BehaviorSubject<VoiceActivity>(VoiceActivity.End)

    const sub = this.recognition.pipe(
      retry(),
      repeat(),
      continuous()
    )
    sub.subscribe({
      next: (res)=>{

        console.log(res)

        if(vadState.value!==VoiceActivity.Start){
          // User has started talking
          vadState.next(VoiceActivity.Start)
        }

        // User has said something
        clearTimeout(this.endTimeout)
        this.endTimeout = setTimeout(() => {
          vadState.next(VoiceActivity.End)
        }, 1500) // fire "end" after 1.5s of inactivity
      },
      error: (e:Error) => {console.error(e)},
      complete: ()=>{console.log("done")}
    })

    return vadState.asObservable()

  }

}
