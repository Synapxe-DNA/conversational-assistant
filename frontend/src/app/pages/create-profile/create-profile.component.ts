import { Component, OnInit } from "@angular/core"
import { ProfileService } from "../../services/profile/profile.service"
import { createId } from "@paralleldrive/cuid2"

@Component({
  selector: "app-create-profile",
  standalone: true,
  imports: [],
  templateUrl: "./create-profile.component.html",
  styleUrl: "./create-profile.component.css",
})
export class CreateProfileComponent implements OnInit {
  constructor(private profileService: ProfileService) {}

  ngOnInit() {
    this.profileService.createProfile({
      id: createId(),
      name: createId().slice(0, 6),
      age: 24,
      existing_conditions: "",
      isMale: true,
    })
  }
}
