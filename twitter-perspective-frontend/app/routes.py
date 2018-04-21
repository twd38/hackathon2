from flask import render_template
from app import app

import jsonpickle
import tweepy as tp
from twython import Twython
import oembed
consumer = oembed.OEmbedConsumer()


#CampaignFinBot
consumer_key = '0mErj1LvShLXydLXQoujly1sl'
consumer_secret = 'OHxc2TwHkaNfq6kDByhnNXqZG4Z9VZ3iS7H3IlaMe9uIjk0W3s'
access_token = '974349318156152832-7OaP8AOzVAzwvc41ZfZZuIS3A8ttPss'
access_secret = 'jhEEFtRWT19snQkcqhiS1Y4v7fDEUAOG4JqQliCRMgHuz'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

searchQuery = 'place:96683cc9126741d1 #nra'

#Maximum number of tweets we want to collect
maxTweets = 1
#The twitter Search API allows up to 100 tweets per query
tweetsPerQry = 1

tweetCount = 0
#Open a text file to save the tweets to
with open('PoGo_USA_Tutorial.json', 'w') as f:

    #Tell the Cursor method that we want to use the Search API (api.search)
    #Also tell Cursor our query, and the maximum number of tweets to return
    for tweet in tp.Cursor(api.search,q=searchQuery).items(maxTweets) :

        #Verify the tweet has place info before writing (It should, if it got past our place filter)
        if tweet.place is not None:

            #Write the JSON format to the text file, and add one to the number of tweets we've collected
            newTweet = jsonpickle.encode(tweet._json, unpicklable=False)
            tweetCount += 1


 # response = consumer.embed('http://www.flickr.com/photos/wizardbt/2584979382/')

    newTweet = tweet.id
    userID= tweet.user.screen_name
    text= tweet.text

    # embed = consumer.embed('https://twitter.com/realDonaldTrump/status/987463564305797126')
    embed = oembed.OEmbedEndpoint('ttps://twitter.com/realDonaldTrump/status/987463564305797126', ['http://*.twitter.com/*'])
    consumer.addEndpoint(embed)

@app.route('/')
@app.route('/index')
def index():
    tweet = {'tweet_display': newTweet}
    return render_template('index.html', title='Home', tweet=tweet, userID=userID, embed=embed, text=text)
