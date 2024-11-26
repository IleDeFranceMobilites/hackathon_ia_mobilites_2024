import { Routes } from '@angular/router';
import { LandingComponent } from './components/landing/landing.component';
import { PreferencesComponent } from './components/preferences/preferences.component';
import { ChatComponent } from './components/chat/chat.component';
import { DirectionsComponent } from './components/directions/directions.component';

export const routes: Routes = [
  {
    path: '',
    component: LandingComponent,
    title: 'Landing',
  }, {
    path: 'preferences',
    component: PreferencesComponent,
    title: 'Preferences',
  },
  {
    path: 'chat',
    component: ChatComponent,
    title: 'Chat',
  },
  {
    path: 'directions',
    component: DirectionsComponent,
    title: 'Directions',
  }
];
