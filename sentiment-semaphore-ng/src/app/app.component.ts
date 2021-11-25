import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Tweets } from './interfaces/request-tweets';
import { TweetService } from './services/tweet.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  results: string = '';
  active: boolean = false;

  listTweets: Tweets[] = [];
  requestForm: FormGroup;
  
  dataTweets = new MatTableDataSource<Tweets>();
  @ViewChild(MatPaginator)
  paginator!: MatPaginator;
  @ViewChild(MatSort)
  sort!: MatSort;

  displayItems: string[] = ["text", "accuracy", "result"]
  //viewTweets: RequestTweets = { account_tweets: "SpiderManMovie", date_tweets: "2021-11-17", number_tweets: 10 };

  constructor(private tweetService: TweetService, private formBuilder: FormBuilder) {
    this.requestForm = this.formBuilder.group({
      account_tweets: ['SpiderManMovie', [Validators.required]],
      date_tweets: ['2021-11-17', [Validators.required]],
      number_tweets: [10, [Validators.required]]
    })
  }

  ngOnInit(): void {
    //this.sendRequest();
  }

  sendRequest() {
    this.tweetService.predictTweets(this.requestForm.value).subscribe({
      error: (err) => console.log(err),
      next: (rest) => {
        this.listTweets = rest.details;
        this.results = rest.mean_text;
        //this.results = "Negativo"
        
        this.dataTweets = new MatTableDataSource<Tweets>(this.listTweets)
        this.dataTweets.sort = this.sort;
        this.dataTweets.paginator = this.paginator

        this.active = true;

        console.log(this.listTweets);
        console.log(this.results)
      },
      complete: () => console.log('Successfull API')
    });
  }

  convertString(percentName: string) {
    var percent = percentName.substr(0, 4)

    var newPercent = new String(percent + " " + "%")
    return newPercent
  }

  title = 'sentiment-semaphore-ng';
}
