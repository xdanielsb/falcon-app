import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable, of } from 'rxjs';
import {
  Graph,
  GraphMetadataForm,
  GraphResponse,
  parseGraph,
} from '../models/graph';
import { ShortestPath } from '../models/shortest-path';
import { ApiUrls } from '../api.urls';

@Injectable({
  providedIn: 'root',
})
export class GraphService {
  constructor(private http: HttpClient) {}

  getGraph(): Observable<Graph> {
    return this.http
      .get<GraphResponse>(ApiUrls.GraphUrl)
      .pipe(map((response) => parseGraph(response)));
  }

  computeOdds(input: GraphMetadataForm): Observable<ShortestPath> {
    return this.http.post<ShortestPath>(ApiUrls.ShortestPathUrl, {
      ...input,
      autonomy: Number.parseInt(<string>input.autonomy || '0'),
    });
  }
}
