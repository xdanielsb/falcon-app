import {
  ChangeDetectionStrategy,
  Component,
  ElementRef,
  EventEmitter,
  Output,
  ViewChild,
} from '@angular/core';
import { ManageFileComponent } from '../manage-file/manage-file.component';

@Component({
  selector: 'app-file-input',
  standalone: true,
  imports: [],
  template: `<input
    type="file"
    #input
    (change)="selectFile($event)"
    [accept]="allowedMimeTypes"
  />`,
  styles: [
    `
      input[type='file'] {
        display: none;
      }
    `,
  ],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FileInputComponent extends ManageFileComponent {
  @Output() selectFileEvent = new EventEmitter<File>();
  @ViewChild('input') input!: ElementRef;

  public selectFile(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0] && this.allowedFile(input.files[0])) {
      this.selectFileEvent.emit(input.files[0]);
      // allows to upload the same file one after another
      input.value = '';
    }
  }
}
