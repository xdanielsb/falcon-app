import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable, of } from 'rxjs';
import {
  Graph,
  GraphMetadataForm,
  GraphResponse,
  parseGraph,
} from '../models/graph';
import { GraphPath } from '../models/graph-path';
import { ApiUrls } from '../api.urls';
import { GraphInfo } from '../models/graph-info';

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

  computeOdds(input: GraphMetadataForm): Observable<GraphPath> {
    return this.http.post<GraphPath>(ApiUrls.FindPathUrl, {
      ...input,
      autonomy: Number.parseInt(<string>input.autonomy || '0'),
    });
  }

  getGraphInfo(): Observable<GraphInfo> {
    return this.http.get<GraphInfo>(ApiUrls.GraphInfoUrl);
  }
}
