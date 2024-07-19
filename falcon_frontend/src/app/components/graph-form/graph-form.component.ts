import {
  Component,
  EventEmitter,
  Input,
  OnChanges,
  Output,
  SimpleChanges,
} from '@angular/core';
import { CommonModule, PercentPipe } from '@angular/common';
import { MatButton } from '@angular/material/button';
import { MatFormField, MatLabel } from '@angular/material/form-field';
import { MatOption, MatSelect } from '@angular/material/select';
import { TranslateModule } from '@ngx-translate/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatInput } from '@angular/material/input';
import { AppForm } from '../../utils/form';
import { Graph, GraphMetadataForm } from '../../models/graph';
import { GraphInfo } from '../../models/graph-info';
import { MatProgressSpinner } from '@angular/material/progress-spinner';

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
    MatProgressSpinner,
  ],
  templateUrl: './graph-form.component.html',
  styleUrl: './graph-form.component.scss',
})
export class GraphFormComponent implements OnChanges {
  form: AppForm<GraphMetadataForm> = this.fb.group({
    sourceId: [null, Validators.required],
    targetId: [null, Validators.required],
    autonomy: [5, Validators.min(0)],
    countdown: [null, Validators.min(0)],
  }) as unknown as AppForm<GraphMetadataForm>;

  @Output() computeOddsEvent = new EventEmitter<GraphMetadataForm>();
  @Input({ required: true }) graph: Graph = { nodes: [], edges: [] };
  @Input({ required: true }) odds!: number | null;
  @Input({ required: true }) minDistance!: number | null;
  @Input({ required: true }) graphInfo: GraphInfo | null = null;
  @Input({ required: true }) loading!: boolean;

  constructor(private fb: FormBuilder) {}

  /** emit events that compute the odds */
  computeOdds(): void {
    if (this.form.value) {
      this.computeOddsEvent.emit(this.form.value as GraphMetadataForm);
    }
  }

  ngOnChanges(changes: SimpleChanges): void {
    if ('graphInfo' in changes) {
      this.form.reset({
        sourceId: this.graphInfo?.sourceId,
        targetId: this.graphInfo?.targetId,
        autonomy: this.graphInfo?.autonomy,
        countdown: null,
      });
    }
  }

  protected readonly Number = Number;
}
