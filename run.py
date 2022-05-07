from twitter import *
from hate_detect import *
import pandas as pd


search_words = input("Keyword to search: ") 
grab_tweets(search_words)

vals = run_all()
all = vals[0]
pos = vals[1]
neg = vals[2]
neu = vals[3]
print("Out of the "+str(all)+" tweets containing the word " + search_words)
print ("Positive tweets: ""{0:.0f}%".format((pos/all) * 100))
print ("Negative tweets: ""{0:.0f}%".format((neg/all) * 100))
print ("Neutral tweets: ""{0:.0f}%".format((neu/all) * 100))

print("The most negative tweet was at a "+str(vals[4]/1000)+"%. It stated "+ vals[6])
print("The most positive tweet was at a "+str(vals[5]/1000)+"%. It stated "+ vals[7])
