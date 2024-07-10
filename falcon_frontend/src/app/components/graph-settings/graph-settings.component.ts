import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { RouterLink } from '@angular/router';
import { MatListItem, MatListItemIcon } from '@angular/material/list';
import { MatIcon } from '@angular/material/icon';
import { MatTooltip } from '@angular/material/tooltip';
import { MatFormField } from '@angular/material/form-field';
import {
  MatOption,
  MatSelect,
  MatSelectModule,
} from '@angular/material/select';

@Component({
  selector: 'app-graph-settings',
  standalone: true,
  imports: [
    CommonModule,
    TranslateModule,
    RouterLink,
    MatListItem,
    MatSelectModule,
    MatIcon,
    MatListItemIcon,
    MatTooltip,
    MatFormField,
    MatSelect,
    MatOption,
  ],
  templateUrl: './graph-settings.component.html',
  styleUrl: './graph-settings.component.scss',
})
export class GraphSettingsComponent {
  readonly languages = [
    {
      value: 'en',
      label: 'GRAPH_MANAGEMENT.LANGUAGE.ENGLISH',
      img: 'assets/countries/us.png',
    },
    {
      value: 'fr',
      label: 'GRAPH_MANAGEMENT.LANGUAGE.FRENCH',
      img: 'assets/countries/fr.png',
    },
    {
      value: 'es',
      label: 'GRAPH_MANAGEMENT.LANGUAGE.SPANISH',
      img: 'assets/countries/es.png',
    },
  ];
  language = this.languages[0];

  constructor(private translate: TranslateService) {
    translate.setDefaultLang('en');
    translate.use('en');
  }

  selectLanguage(code: string): void {
    this.translate.use(code);
    this.language =
      this.languages.find((lang) => lang.value === code) || this.languages[0];
  }
}
