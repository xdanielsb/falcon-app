import {
  ChangeDetectorRef,
  Component,
  Input,
  OnChanges,
  SimpleChanges,
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgxGraphModule } from '@swimlane/ngx-graph';
import { Graph } from '../../models/graph';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-graph-preview',
  standalone: true,
  imports: [CommonModule, NgxGraphModule],
  templateUrl: './graph-preview.component.html',
  styleUrl: './graph-preview.component.scss',
})
export class GraphPreviewComponent implements OnChanges {
  @Input({ required: true }) graph: Graph | null = null;
  update$: Subject<any> = new Subject();
  zoomToFit$: Subject<any> = new Subject();

  constructor(private ref: ChangeDetectorRef) {}

  ngOnChanges(changes: SimpleChanges): void {
    this.update$.next(true);
    this.zoomToFit$.next({ force: true, autoCenter: true });
    this.ref.detectChanges();
  }
}
