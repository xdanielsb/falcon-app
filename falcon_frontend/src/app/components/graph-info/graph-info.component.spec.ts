import { ComponentFixture, TestBed } from '@angular/core/testing';
import { GraphInfoComponent } from './graph-info.component';
import { provideMockStore } from '@ngrx/store/testing';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { importProvidersFrom } from '@angular/core';
import { TranslateModule } from '@ngx-translate/core';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';

describe('GraphInfoComponent', () => {
  let component: GraphInfoComponent;
  let fixture: ComponentFixture<GraphInfoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GraphInfoComponent, NoopAnimationsModule],
      providers: [
        provideMockStore(),
        provideHttpClient(),
        provideHttpClientTesting(),
        importProvidersFrom(TranslateModule.forRoot({})),
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(GraphInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
