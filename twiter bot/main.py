import tweepy as twitter
import keys
import time
import streamlit

# API SETUP

api_key=keys.api_key
api_key_secret=keys.api_key_secret
access_token=keys.access_token
access_token_secret=keys.access_token_secret
bearer_token=keys.bearer_token

authenticator=twitter.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)


api=twitter.API(authenticator, wait_on_rate_limit=True)

def twitter_retweet(hashtag, delay):
    while True:
        for tweet in twitter.Cursor(api.search, q=hashtag, rpp=10).items(10):
            try:
                tweet_id=dict(tweet._json)['id']
                tweet_text=dict(tweet._json)['text']
                
                print('id: ' + str(tweet_id))
                print('text: '+ str(tweet_text))
                
                api.retweet(tweet_id)
                
            except twitter.TweepError as error:
                print(error.reason)
                
        time.sleep(delay)


twitter_retweet("#nallagang", 10)



    
   
