import { Component, Input, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButton } from '@angular/material/button';
import { MatFormField, MatLabel } from '@angular/material/form-field';
import { MatOption, MatSelect } from '@angular/material/select';
import { TranslateModule } from '@ngx-translate/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { MatInput } from '@angular/material/input';
import { AppForm } from '../../utils/form';
import { GraphMetadataForm } from '../../models/graph';

@Component({
  selector: 'app-graph-form',
  standalone: true,
  imports: [
    CommonModule,
    MatButton,
    MatFormField,
    MatSelect,
    MatOption,
    MatLabel,
    TranslateModule,
    ReactiveFormsModule,
    MatInput,
  ],
  templateUrl: './graph-form.component.html',
  styleUrl: './graph-form.component.scss',
})
export class GraphFormComponent {
  form: AppForm<GraphMetadataForm> = this.fb.group({
    departure: [null, Validators.required],
    destination: [null, Validators.required],
    autonomy: [5, Validators.min(1)],
  }) as AppForm<GraphMetadataForm>;

  // todo: replace by input create a service to get the nodes
  nodes = [{ id: 1, label: 'hello' }];
  constructor(private fb: FormBuilder) {}

  computeOdds(): void {
    // tode: implement service to get the odds
  }
}
