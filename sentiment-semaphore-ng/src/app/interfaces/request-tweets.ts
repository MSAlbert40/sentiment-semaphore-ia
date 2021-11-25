export interface RequestTweets {
    account_tweets: string;
    date_tweets: string;
    number_tweets: number;
}

export interface Tweets {
    accurancy: string;
    date: string;
    result: string;
    text: string;
}

export interface MessageResponse<T> {
    details: T;
    mean: number;
    mean_text: string;
}