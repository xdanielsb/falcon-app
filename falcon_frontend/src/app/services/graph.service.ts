import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable, of } from 'rxjs';
import { GraphMetadataForm, GraphResponse, parseGraph } from '../models/graph';
import { ShortestPath } from '../models/shortest-path';
import { ApiUrls } from '../api.urls';

@Injectable({
  providedIn: 'root',
})
export class GraphService {
  constructor(private http: HttpClient) {}

  getGraph() {
    return this.http
      .get<GraphResponse>(ApiUrls.GraphUrl)
      .pipe(map((response) => parseGraph(response)));
  }

  computeOdds(input: GraphMetadataForm) {
    return this.http.post<ShortestPath>(ApiUrls.ShortestPathUrl, {
      ...input,
      autonomy: Number.parseInt(<string>input.autonomy || '0'),
    });
  }
}
