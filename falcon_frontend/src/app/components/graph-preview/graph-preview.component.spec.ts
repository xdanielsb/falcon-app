import { ComponentFixture, TestBed } from '@angular/core/testing';
import { GraphPreviewComponent } from './graph-preview.component';

describe('GraphPreviewComponent', () => {
  let component: GraphPreviewComponent;
  let fixture: ComponentFixture<GraphPreviewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GraphPreviewComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(GraphPreviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
