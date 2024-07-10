import { FormControl, FormGroup } from '@angular/forms';

export type AppForm<T> = FormGroup<{
  [K in keyof T]: FormControl<T[K]>;
}>;

export type TableRow = {
  value?: string | number;
  label: string;
};
