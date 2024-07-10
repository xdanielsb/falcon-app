import { ComponentFixture, TestBed } from '@angular/core/testing';
import { GraphSettingsComponent } from './graph-settings.component';

describe('GraphSettingsComponent', () => {
  let component: GraphSettingsComponent;
  let fixture: ComponentFixture<GraphSettingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GraphSettingsComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(GraphSettingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
