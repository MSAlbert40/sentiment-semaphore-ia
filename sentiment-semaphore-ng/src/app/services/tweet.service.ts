import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { MessageResponse, RequestTweets, Tweets } from '../interfaces/request-tweets';

@Injectable({
  providedIn: 'root'
})
export class TweetService {

  constructor(private http: HttpClient) { }

  predictTweets(body: RequestTweets): Observable<MessageResponse<Tweets[]>> {
    return this.http.post<MessageResponse<Tweets[]>>(environment.apiURL + 'sentiment-analysis', body);
  }

}
