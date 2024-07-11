import { ComponentFixture, TestBed } from '@angular/core/testing';
import { GraphPreviewComponent } from './graph-preview.component';
import { provideMockStore } from '@ngrx/store/testing';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { importProvidersFrom } from '@angular/core';
import { TranslateModule } from '@ngx-translate/core';

describe('GraphPreviewComponent', () => {
  let component: GraphPreviewComponent;
  let fixture: ComponentFixture<GraphPreviewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GraphPreviewComponent],
      providers: [
        provideMockStore(),
        provideHttpClient(),
        provideHttpClientTesting(),
        importProvidersFrom(TranslateModule.forRoot({})),
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(GraphPreviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
