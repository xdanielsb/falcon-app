import {
  ChangeDetectorRef,
  Component,
  Input,
  OnChanges,
  SimpleChanges,
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { GraphInfo } from '../../models/graph-info';
import {
  MatCell,
  MatColumnDef,
  MatHeaderCell,
  MatHeaderRow,
  MatRow,
  MatTable,
  MatTableDataSource,
  MatTableModule,
} from '@angular/material/table';
import { TableRow } from '../../utils/form';

@Component({
  selector: 'app-graph-info',
  standalone: true,
  imports: [
    CommonModule,
    TranslateModule,
    MatTableModule,
    MatHeaderCell,
    MatCell,
    MatTable,
    MatHeaderRow,
    MatRow,
    MatColumnDef,
  ],
  templateUrl: './graph-info.component.html',
  styleUrl: './graph-info.component.scss',
})
export class GraphInfoComponent implements OnChanges {
  @Input({ required: true }) graphInfo: GraphInfo | null = null;

  graphDataSource = new MatTableDataSource<TableRow>([]);
  displayedColumns: string[] = ['label', 'value'];
  constructor(private translateService: TranslateService) {}

  ngOnChanges(changes: SimpleChanges): void {
    this.graphDataSource.data = [
      {
        label: this.translateService.instant(
          'GRAPH_MANAGEMENT.NUMBER_OF_NODES',
        ),
        value: this.graphInfo?.numberOfNodes || '',
      },
      {
        label: this.translateService.instant(
          'GRAPH_MANAGEMENT.NUMBER_OF_EDGES',
        ),
        value: this.graphInfo?.numberOfEdges,
      },
      {
        label: 'GRAPH_MANAGEMENT.NUMBER_OF_HUNTERS',
        value: this.translateService.instant(this.graphInfo?.hunters.length),
      },
      {
        label: this.translateService.instant('GRAPH_MANAGEMENT.COUNTDOWN'),
        value: this.graphInfo?.countDown,
      },
    ];
  }
}
