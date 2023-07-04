import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PredictionService {

  constructor(private _http: HttpClient) { }

  public postCandidateData(candidateData: object): Observable<string>{
    //FRONT INSTRUCTION HERE
    return this._http.post<string>('', candidateData);
  }
}
