from unicodedata import normalize
import tweepy as tw
import pandas as pd

def getTweets(account: str, date: str, number):
    consumerKey = 'BmIa58mOPL6Dj6gUrVPYih6kn'
    consumerSecret = 'Jo5Gd3cXIYplaE6QxpTTV4w5EqDkHa5lRoX1IUVSEA52U1siUz'

    accessToken = '1053826438724575232-4IDIue6OBy73FzHNHv6qbxrudNE05u'
    accessTokenSecret = 'ahVX5doKMWRHOavtgAoB64C3xYzlJ3YON1rKdqvjRnvpH'

    auth = tw.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tw.API(auth, wait_on_rate_limit = True)

    allTweets = tw.Cursor(api.search_tweets, 
                        q = "@" + account + " -filter:retweets",
                        lang = "es",
                        tweet_mode = 'extended',
                        since = date).items(number)

    transTab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    usersTweets = [[
        tweet._json['id_str'],
        str(tweet._json['created_at']),
        normalize('NFKC', normalize('NFKD', tweet._json['full_text'].rstrip()).translate(transTab))
    ] for tweet in allTweets]
    tweetFrame = pd.DataFrame(data = usersTweets, columns = ['userCode', 'date', 'text'])
    tweetFrame.to_csv('dataTweets.csv', index = False)