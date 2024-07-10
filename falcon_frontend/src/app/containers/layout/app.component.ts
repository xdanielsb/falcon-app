import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import {
  MatDrawer,
  MatDrawerContainer,
  MatDrawerContent,
} from '@angular/material/sidenav';
import { GraphFormComponent } from '../../components/graph-form/graph-form.component';
import { GraphSettingsComponent } from '../../components/graph-settings/graph-settings.component';
import { GraphService } from '../../services/graph.service';
import { GraphMetadataForm } from '../../models/graph';
import { TranslateModule } from '@ngx-translate/core';

@Component({
  standalone: true,
  imports: [
    RouterModule,
    MatDrawerContainer,
    MatDrawer,
    MatDrawerContent,
    GraphFormComponent,
    GraphSettingsComponent,
    TranslateModule,
  ],
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  graph$ = this.graphService.getGraph();
  graph: any;
  odds: number | null = null;
  constructor(private graphService: GraphService) {
    this.graph$.subscribe((graph) => {
      this.graph = graph;
      console.log(graph);
    });
  }

  computeOdds(input: GraphMetadataForm) {
    this.graphService.computeOdds(input).subscribe((res) => {
      this.odds = res.probability;
    });
  }
}
