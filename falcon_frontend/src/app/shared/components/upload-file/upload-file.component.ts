import {
  ChangeDetectionStrategy,
  Component,
  EventEmitter,
  Output,
} from '@angular/core';
import { NgxFileDropEntry, NgxFileDropModule } from 'ngx-file-drop';
import { ManageFileComponent } from '../manage-file/manage-file.component';

@Component({
  selector: 'app-upload-file',
  standalone: true,
  imports: [NgxFileDropModule],
  template: `
    <ngx-file-drop (onFileDrop)="droppedFile($event)">
      <ng-template ngx-file-drop-content-tmp>
        <ng-content />
      </ng-template>
    </ngx-file-drop>
  `,
  styles: ['ngx-file-drop {width: 100%}'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class UploadFileComponent extends ManageFileComponent {
  @Output() dragFileEvent = new EventEmitter<File>();

  public droppedFile(files: NgxFileDropEntry[]): void {
    const droppedFile: NgxFileDropEntry = files[0];
    if (droppedFile.fileEntry.isFile) {
      const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
      fileEntry.file((file: File) => {
        if (this.allowedFile(file)) {
          this.dragFileEvent.emit(file);
        }
      });
    }
  }
}
