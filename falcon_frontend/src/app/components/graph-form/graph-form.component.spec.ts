import { ComponentFixture, TestBed } from '@angular/core/testing';
import { GraphFormComponent } from './graph-form.component';
import { provideMockStore } from '@ngrx/store/testing';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { importProvidersFrom } from '@angular/core';
import { TranslateModule } from '@ngx-translate/core';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';

describe('GraphFormComponent', () => {
  let component: GraphFormComponent;
  let fixture: ComponentFixture<GraphFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GraphFormComponent, NoopAnimationsModule],
      providers: [
        provideMockStore(),
        provideHttpClient(),
        provideHttpClientTesting(),
        importProvidersFrom(TranslateModule.forRoot({})),
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(GraphFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
