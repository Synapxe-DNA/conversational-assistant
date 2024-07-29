import {Injectable} from '@angular/core';
import {final, SpeechRecognitionService} from "@ng-web-apis/speech";
import {BehaviorSubject, Observable, repeat, retry} from "rxjs";
import {VoiceActivity} from "../../types/voice-activity.type";

@Injectable({
  providedIn: 'root'
})
export class VadService {

  constructor(
    private recognition: SpeechRecognitionService
  ) {

  }

  start():Observable<VoiceActivity>{

    const vadState = new BehaviorSubject<VoiceActivity>(VoiceActivity.End)

    const sub = this.recognition.pipe(
      repeat(),
      final(),
      retry()
    )
    sub.subscribe({
      next: (res)=>{

        if(!res.length && vadState.value!==VoiceActivity.Start){
          // User has started talking
          vadState.next(VoiceActivity.Start)
        }

        if(res.length){
          // User has finished speaking
          vadState.next(VoiceActivity.End)
        }
      },
      error: (e:Error) => {console.error(e)},
      complete: ()=>{console.log("done")}
    })

    return vadState.asObservable()

  }

}
