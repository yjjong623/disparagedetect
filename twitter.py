import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
def grab_tweets(search_words): 
    auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAPS%2FcAEAAAAAzsx4S0zMOU1ybsBviCuq8GQ8AuI%3DH8mn270E7VFhDSez8QqfAk8PcpC0SQu0GbLGLI4qZI9E2u445h")
    api = tweepy.API(auth)
    
    csvFile = open('file-name.csv', 'w+')
    csvWriter = csv.writer(csvFile)
    
     # enter your words
    new_search = search_words + " -filter:retweets" + " -filter:users"

    
    for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=100,
                            lang="en",
                            since_id=0).items():
        if search_words in (str(tweet.text.encode('utf-8'))):
            csvWriter.writerow([tweet.text.encode('utf-8')])


