import {
  Component,
  EventEmitter,
  Input,
  OnChanges,
  Output,
  SimpleChanges,
  ViewChild,
} from '@angular/core';
import { CommonModule, PercentPipe } from '@angular/common';
import { MatButton, MatMiniFabButton } from '@angular/material/button';
import { MatFormField, MatLabel } from '@angular/material/form-field';
import { MatOption, MatSelect } from '@angular/material/select';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatInput } from '@angular/material/input';
import { AppForm } from '../../utils/form';
import { Graph, GraphMetadataForm } from '../../models/graph';
import { GraphInfo } from '../../models/graph-info';
import { MatProgressSpinner } from '@angular/material/progress-spinner';
import { UploadFileComponent } from '../../shared/components/upload-file/upload-file.component';
import { FileInputComponent } from '../../shared/components/file-input/file-input.component';
import { ToastrService } from 'ngx-toastr';
import { MatIcon } from '@angular/material/icon';

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
    UploadFileComponent,
    FileInputComponent,
    MatIcon,
    MatMiniFabButton,
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
    empireInfo: [null],
  }) as unknown as AppForm<GraphMetadataForm>;

  @ViewChild('inputComponent') inputComponent?: FileInputComponent;
  public file: File | null = null;
  public uploadingFile = false;
  protected readonly Number = Number;

  @Output() computeOddsEvent = new EventEmitter<GraphMetadataForm>();
  @Input({ required: true }) graph: Graph = { nodes: [], edges: [] };
  @Input({ required: true }) odds!: number | null;
  @Input({ required: true }) minDistance!: number | null;
  @Input({ required: true }) graphInfo: GraphInfo | null = null;
  @Input({ required: true }) loading!: boolean;

  constructor(
    private toastrService: ToastrService,
    private translateService: TranslateService,
    private fb: FormBuilder,
  ) {}

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

  browseFile(): void {
    this.inputComponent?.input.nativeElement.click();
  }

  handleFile(file: File): void {
    this.file = file;
    this.uploadingFile = true;
    if (this.file) {
      const reader = new FileReader();
      reader.onload = (event: any) => {
        try {
          const jsonObject = JSON.parse(event.target.result);
          const jsonString = JSON.stringify(jsonObject);
          if (jsonObject['countdown'] !== undefined) {
            this.form.patchValue({
              countdown: Number(jsonObject['countdown']),
            });
            this.toastrService.success(
              this.translateService.instant(
                'GRAPH_MANAGEMENT.SUCCESS_READING_FILE',
              ),
            );
          }
          this.form.patchValue({ empireInfo: jsonString });
        } catch (e) {
          this.toastrService.error(
            this.translateService.instant(
              'GRAPH_MANAGEMENT.ERROR_READING_FILE',
            ),
          );
        }
      };

      reader.readAsText(this.file);
    }
  }

  clearEmpireInfo(): void {
    this.form.patchValue({ empireInfo: null });
    this.file = null;
  }
}
