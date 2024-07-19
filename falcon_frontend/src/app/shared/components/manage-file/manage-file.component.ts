import {
  ChangeDetectionStrategy,
  Component,
  inject,
  Input,
} from '@angular/core';
import { NgxFileDropModule } from 'ngx-file-drop';
import { MimeTypes } from '../../utils/file';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-manage-file',
  standalone: true,
  imports: [NgxFileDropModule],
  template: ``,
  styles: [''],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ManageFileComponent {
  @Input() allowedMimeTypes: MimeTypes[] = [MimeTypes.JSON];
  @Input() forbidNonAsciiFilename = false;
  private _snackBard: MatSnackBar = inject(MatSnackBar);
  protected allowedFile(file: File): boolean {
    if (!this.allowedMimeTypes.includes(file.type as MimeTypes)) {
      this._snackBard.open('Invalid mime type, only json allowed', undefined);
      return false;
    }
    return true;
  }
}
