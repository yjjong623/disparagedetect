from contextvars import Token
import pandas as pd
import nltk
import nltk.corpus 

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


nltk.download('punkt')

df = pd.read_csv("./file-name.csv")

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def sentiment_scores(sentence, most_neg, most_pos, neg_phrase, pos_phrase):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    # print("Overall sentiment dictionary is : ", sentiment_dict)
    # print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    # print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    # print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    # print("Sentence Overall Rated As", end = " ")
    if sentiment_dict['neg']*100000 >= most_neg: 
        most_neg = sentiment_dict['neg']*100000
        neg_phrase = sentence

    if sentiment_dict['pos']*100000 >= most_pos:
        most_pos = sentiment_dict['pos']*100000
        pos_phrase = sentence

    if sentiment_dict['compound'] >= 0.05 :
        return(1, most_neg, neg_phrase, most_pos, pos_phrase)
    elif sentiment_dict['compound'] <= - 0.05 :
        return(-1, most_neg, neg_phrase, most_pos, pos_phrase)
    else :
        return (0, most_neg, neg_phrase, most_pos, pos_phrase)

def run_all():
    neg = 0
    pos = 0
    neu = 0

    most_neg = 0
    most_pos = 0
    neg_phrase = ""
    pos_phrase = ""

    for i in range(len(df)):
        value = sentiment_scores(df.iloc[i, 0], most_neg, most_pos, neg_phrase, pos_phrase)
        if value[0] == -1:
            neg = neg + 1
        elif value[0] == 0:
            neu +=1 
        else: 
            pos = pos + 1
        most_neg = value[1]
        most_pos = value[3]
        neg_phrase = value[2]
        pos_phrase = value[4]

    # print(most_neg)
    # print(most_pos)
    # print(neg_phrase)
    # print(pos_phrase)
    return (pos+neg+neu, pos, neg, neu, most_neg, most_pos, neg_phrase, pos_phrase)

# run_all()