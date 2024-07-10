import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';
import { RouterLink } from '@angular/router';
import { MatListItem, MatListItemIcon } from '@angular/material/list';
import { MatIcon } from '@angular/material/icon';
import { MatTooltip } from '@angular/material/tooltip';

@Component({
  selector: 'app-graph-settings',
  standalone: true,
  imports: [
    CommonModule,
    TranslateModule,
    RouterLink,
    MatListItem,
    MatIcon,
    MatListItemIcon,
    MatTooltip,
  ],
  templateUrl: './graph-settings.component.html',
  styleUrl: './graph-settings.component.scss',
})
export class GraphSettingsComponent {}
