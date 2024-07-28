import { AfterViewInit, Injectable, OnInit } from "@angular/core"
import { NgxIndexedDBService } from "ngx-indexed-db"
import { Profile } from "../../types/profile.type"
import { BehaviorSubject } from "rxjs"
import {MessageService} from "primeng/api";

@Injectable({
  providedIn: "root",
})
export class ProfileService implements OnInit {
  $profiles: BehaviorSubject<Profile[]> = new BehaviorSubject<Profile[]>([])

  constructor(
    private dbService: NgxIndexedDBService,
  ) {
    this.dbService.getAll<Profile>("profiles").subscribe((v) => {
      this.$profiles.next(v)
    })
  }

  ngOnInit() {}

  createProfile(profile: Profile) {
    this.dbService.add("profiles", { ...profile }).subscribe(() => {
      this.$profiles.next([...this.$profiles.value, profile])
    })
  }

  getProfiles(): BehaviorSubject<Profile[]> {
    return this.$profiles
  }

  deleteProfile(id: string) {
    this.dbService.delete<Profile>("profiles", id).subscribe()
    this.$profiles.next(this.$profiles.value.filter((p) => p.id !== id))
  }
}
