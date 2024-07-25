import {AfterViewInit, Component, Input, OnInit} from '@angular/core';
import {Profile} from "../../../types/profile.type";
import {ActivatedRoute, Router} from "@angular/router";
import {NgOptimizedImage} from "@angular/common";

@Component({
  selector: 'app-navbar-profile-link',
  standalone: true,
  imports: [
    NgOptimizedImage
  ],
  templateUrl: './navbar-profile-link.component.html',
  styleUrl: './navbar-profile-link.component.css'
})
export class NavbarProfileLinkComponent implements OnInit {

  @Input() profile!:Profile

  isActive:boolean = false

  constructor(
    private router: Router
  ) {
  }

  ngOnInit() {
    const currentPath = this.router.url.split('/')

    if(currentPath.length >= 3 && currentPath[1] === 'chat'){
      if(
        (currentPath[2] === this.profile.id) ||
        (currentPath[2] === "general" && !this.profile.id)
      ) {
        this.isActive = true
      }
    }
  }

  getProfileDescription():string {
    if(this.profile.id===""){
      return "No profile set"
    }

    return `${this.profile.details.isMale?'Male':'Female'}, ${this.profile.details.age} years old`
  }

}
