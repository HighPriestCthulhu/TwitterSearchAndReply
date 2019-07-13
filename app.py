import tweepy
import json
from datetime import datetime, date, time, timedelta
from pword import ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret
from tweepy import Stream
from tweepy.streaming import StreamListener

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

bot = tweepy.API(auth)


try:
    bot.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def WhenFound(data):
    try:
        bot.retweet(data['id'])
        bot.create_friendship(data['user']['id'])
    except:
        pass

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            if not ("retweeted_status" in json.loads(data) or "quoted_status_id" in json.loads(data)):
                with open('python.json', 'a') as f:
                    f.write(data[0:-1])
                    WhenFound(json.loads(data))
                    return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Retweet to win OR retweet for OR retweet'])
