import {
  ApplicationConfig,
  importProvidersFrom,
  provideZoneChangeDetection,
} from "@angular/core";
import { provideRouter } from "@angular/router";

import { routes } from "./app.routes";
import { BrowserModule } from "@angular/platform-browser";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { NgxIndexedDBModule } from "ngx-indexed-db";
import { NgxIndexedDbConfig } from "./configs/ngx-indexed-db/ngx-indexed-db.config";
import {
  LucideAngularModule,
  MessageSquare,
  Mic,
  Settings,
  User,
  UserRoundPlus,
  Send,
} from "lucide-angular";
import { ToastModule } from "primeng/toast";

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
        Settings,
        Send,
      })
    ),
    importProvidersFrom(ToastModule),
  ],
};
