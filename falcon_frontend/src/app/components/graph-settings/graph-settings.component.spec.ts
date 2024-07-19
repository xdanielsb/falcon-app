import { ComponentFixture, TestBed } from '@angular/core/testing';
import { GraphSettingsComponent } from './graph-settings.component';
import { provideMockStore } from '@ngrx/store/testing';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { importProvidersFrom } from '@angular/core';
import { TranslateModule } from '@ngx-translate/core';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from '../../containers/layout/app.component';

describe('GraphSettingsComponent', () => {
  let component: GraphSettingsComponent;
  let fixture: ComponentFixture<GraphSettingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GraphSettingsComponent, NoopAnimationsModule],
      providers: [
        provideMockStore(),
        provideHttpClient(),
        provideHttpClientTesting(),
        importProvidersFrom(TranslateModule.forRoot({})),
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(GraphSettingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should render title', () => {
    const fixture = TestBed.createComponent(AppComponent);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h2')?.textContent).toContain(
      'GRAPH_MANAGEMENT.TITLE',
    );
  });
});
