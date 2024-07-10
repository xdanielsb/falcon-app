import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';

@Component({
  selector: 'app-graph-settings',
  standalone: true,
  imports: [CommonModule, TranslateModule],
  templateUrl: './graph-settings.component.html',
  styleUrl: './graph-settings.component.css',
})
export class GraphSettingsComponent {}
