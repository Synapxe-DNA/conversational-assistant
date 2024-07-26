import {
  ApplicationConfig,
  importProvidersFrom,
  provideZoneChangeDetection,
} from "@angular/core";
import { provideRouter } from "@angular/router";

import { routes } from "./app.routes";
import { BrowserModule } from "@angular/platform-browser";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import {
  LucideAngularModule,
  UserRoundPlus,
  Mic,
  MessageSquare,
  User,
} from "lucide-angular";
import { NgxIndexedDBModule } from "ngx-indexed-db";
import { NgxIndexedDbConfig } from "./configs/ngx-indexed-db/ngx-indexed-db.config";

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    importProvidersFrom(BrowserModule),
    importProvidersFrom(BrowserAnimationsModule),
    importProvidersFrom(NgxIndexedDBModule.forRoot(NgxIndexedDbConfig)),
    importProvidersFrom(
      LucideAngularModule.pick({
        UserRoundPlus,
        Mic,
        MessageSquare,
        User,
      })
    ),
  ],
};
