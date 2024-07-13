import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';
import { MatButton } from '@angular/material/button';

@Component({
  selector: 'app-graph-options',
  standalone: true,
  imports: [CommonModule, TranslateModule, MatButton],
  templateUrl: './graph-options.component.html',
  styleUrl: './graph-options.component.scss',
})
export class GraphOptionsComponent {
  @Output() createRandomGraphEvent = new EventEmitter<void>();

  createRandomGraph(): void {
    this.createRandomGraphEvent.emit();
  }
}
