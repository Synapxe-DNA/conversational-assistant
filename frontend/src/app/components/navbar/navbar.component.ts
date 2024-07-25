import { Component } from '@angular/core';
import {NavbarLogoGroupComponent} from "./navbar-logo-group/navbar-logo-group.component";
import {NavbarLineComponent} from "./navbar-line/navbar-line.component";
import {NavbarProfileLinkComponent} from "./navbar-profile-links/navbar-profile-link.component";
import {NavbarProfileCreateComponent} from "./navbar-profile-create/navbar-profile-create.component";
import {GeneralProfile} from "../../types/profile.type";

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [
    NavbarLogoGroupComponent,
    NavbarLineComponent,
    NavbarProfileLinkComponent,
    NavbarProfileCreateComponent
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

  protected readonly GeneralProfile = GeneralProfile;
}
