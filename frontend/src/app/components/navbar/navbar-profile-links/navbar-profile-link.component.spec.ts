import { ComponentFixture, TestBed } from "@angular/core/testing";

import { NavbarProfileLinkComponent } from "./navbar-profile-link.component";

describe("NavbarProfileLinksComponent", () => {
  let component: NavbarProfileLinkComponent;
  let fixture: ComponentFixture<NavbarProfileLinkComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NavbarProfileLinkComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(NavbarProfileLinkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("should create", () => {
    expect(component).toBeTruthy();
  });
});
