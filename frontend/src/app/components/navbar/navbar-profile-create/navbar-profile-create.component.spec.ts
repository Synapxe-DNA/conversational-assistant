import { ComponentFixture, TestBed } from "@angular/core/testing"

import { NavbarProfileCreateComponent } from "./navbar-profile-create.component"

describe("NavbarProfileCreateComponent", () => {
  let component: NavbarProfileCreateComponent
  let fixture: ComponentFixture<NavbarProfileCreateComponent>

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NavbarProfileCreateComponent],
    }).compileComponents()

    fixture = TestBed.createComponent(NavbarProfileCreateComponent)
    component = fixture.componentInstance
    fixture.detectChanges()
  })

  it("should create", () => {
    expect(component).toBeTruthy()
  })
})
