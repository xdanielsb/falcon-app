import {
  Component,
  EventEmitter,
  Input,
  OnChanges,
  Output,
  SimpleChanges,
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButton } from '@angular/material/button';
import { MatFormField, MatLabel } from '@angular/material/form-field';
import { MatOption, MatSelect } from '@angular/material/select';
import { TranslateModule } from '@ngx-translate/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatInput } from '@angular/material/input';
import { AppForm } from '../../utils/form';
import { Graph, GraphMetadataForm } from '../../models/graph';
import { GraphInfo } from '../../models/graph-info';

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
export class GraphFormComponent implements OnChanges {
  form: AppForm<GraphMetadataForm> = this.fb.group({
    sourceId: [null, Validators.required],
    targetId: [null, Validators.required],
    autonomy: [5, Validators.min(0)],
  }) as AppForm<GraphMetadataForm>;

  @Output() computeOddsEvent = new EventEmitter<GraphMetadataForm>();
  @Input({ required: true }) graph!: Graph;
  @Input({ required: true }) odds!: number | null;
  @Input({ required: true }) graphInfo: GraphInfo | null = null;
  constructor(private fb: FormBuilder) {}

  computeOdds(): void {
    if (this.form.value) {
      this.computeOddsEvent.emit(this.form.value as GraphMetadataForm);
    }
  }

  ngOnChanges(changes: SimpleChanges): void {
    if ('graphInfo' in changes) {
      this.form.reset({
        sourceId: this.graphInfo?.sourceId.toString(),
        targetId: this.graphInfo?.targetId.toString(),
        autonomy: this.graphInfo?.autonomy,
      });
    }
  }
}
