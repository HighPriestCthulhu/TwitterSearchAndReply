import tweepy
import json
from datetime import datetime
from pword import ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret
from tweepy import Stream
from tweepy.streaming import StreamListener


auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret) #set up login details
auth.set_access_token(AccessToken, AccessTokenSecret)   #create connection

bot = tweepy.API(auth)

"""
  #####  ####### ######  #######     #####  #######    #    ######  #######
 #     # #     # #     # #          #     #    #      # #   #     #    #
 #       #     # #     # #          #          #     #   #  #     #    #
 #       #     # #     # #####       #####     #    #     # ######     #
 #       #     # #     # #                #    #    ####### #   #      #
 #     # #     # #     # #          #     #    #    #     # #    #     #
  #####  ####### ######  #######     #####     #    #     # #     #    #

"""
try:
    bot.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

"""
.##......##.##.....##.########.##....##....########..#######..##.....##.##....##.########.
.##..##..##.##.....##.##.......###...##....##.......##.....##.##.....##.###...##.##.....##
.##..##..##.##.....##.##.......####..##....##.......##.....##.##.....##.####..##.##.....##
.##..##..##.#########.######...##.##.##....######...##.....##.##.....##.##.##.##.##.....##
.##..##..##.##.....##.##.......##..####....##.......##.....##.##.....##.##..####.##.....##
.##..##..##.##.....##.##.......##...###....##.......##.....##.##.....##.##...###.##.....##
..###..###..##.....##.########.##....##....##........#######...#######..##....##.########.
"""
def WhenFound(data):
    try:
        bot.retweet(data['id'])
        bot.create_friendship(data['user']['id'])
        bot.create_favorite(data['id'])
        print(bot.rate_limit_status())
    except:
        print('fail at whenfound')

"""
.##.......####..######..########.########.##....##.########.########.
.##........##..##....##....##....##.......###...##.##.......##.....##
.##........##..##..........##....##.......####..##.##.......##.....##
.##........##...######.....##....######...##.##.##.######...########.
.##........##........##....##....##.......##..####.##.......##...##..
.##........##..##....##....##....##.......##...###.##.......##....##.
.########.####..######.....##....########.##....##.########.##.....##
"""
class MyListener(StreamListener): #extends class
    def on_data(self, data):
        try:
            #print("trying ")
            if not ("retweeted_status" in json.loads(data) or "quoted_status_id" in json.loads(data)):
                with open('python.json', 'a') as f:
                    print("      win ")
                    f.write(data[0:-1])
                    WhenFound(json.loads(data))
                    return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
"""
..######...#######..##.....##.##.....##....###....##....##.########...######.
.##....##.##.....##.###...###.###...###...##.##...###...##.##.....##.##....##
.##.......##.....##.####.####.####.####..##...##..####..##.##.....##.##......
.##.......##.....##.##.###.##.##.###.##.##.....##.##.##.##.##.....##..######.
.##.......##.....##.##.....##.##.....##.#########.##..####.##.....##.......##
.##....##.##.....##.##.....##.##.....##.##.....##.##...###.##.....##.##....##
..######...#######..##.....##.##.....##.##.....##.##....##.########...######.
"""
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Retweet to win','To Enter retweet','RT to win'])