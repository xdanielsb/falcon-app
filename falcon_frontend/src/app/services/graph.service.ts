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

  /** This method returns the graph {nodes, edges}, it helps for having a preview */
  getGraph(): Observable<Graph> {
    return this.http
      .get<GraphResponse>(ApiUrls.GraphUrl)
      .pipe(map((response) => parseGraph(response)));
  }

  /** This method returns the odds of the path, as well as the path and
   * the distances from the origin to each node in the path
   * @param input origin, destiny ids and the autonomy to recompute the odds
   * the default value is the value store in the db
   * */
  computeOdds(input: GraphMetadataForm): Observable<GraphPath> {
    return this.http.post<GraphPath>(ApiUrls.FindPathUrl, {
      ...input,
      countdown: input.countdown === null ? null : Number(input.countdown),
      autonomy: input.autonomy === null ? null : Number(input.autonomy),
    });
  }

  /** This method returns the info of the graph */
  getGraphInfo(): Observable<GraphInfo> {
    return this.http.get<GraphInfo>(ApiUrls.GraphInfoUrl);
  }

  /** This method creates a new graph
   * @param random if true the graph will be random otherwise
   * it will be the default graph;
   * */
  createGraph(random: boolean): Observable<Graph> {
    return this.http
      .post<GraphResponse>(ApiUrls.CreateGraphUrl, { random })
      .pipe(map((response) => parseGraph(response)));
  }
}
