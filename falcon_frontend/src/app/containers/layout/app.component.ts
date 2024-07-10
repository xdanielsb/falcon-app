import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import {
  MatDrawer,
  MatDrawerContainer,
  MatDrawerContent,
} from '@angular/material/sidenav';
import { GraphFormComponent } from '../../components/graph-form/graph-form.component';
import { GraphSettingsComponent } from '../../components/graph-settings/graph-settings.component';

@Component({
  standalone: true,
  imports: [
    RouterModule,
    MatDrawerContainer,
    MatDrawer,
    MatDrawerContent,
    GraphFormComponent,
    GraphSettingsComponent,
  ],
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'falcon_frontend';
}
