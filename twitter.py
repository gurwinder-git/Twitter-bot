import tweepy
import time
import json


auth = tweepy.OAuthHandler('xxxxxxxxxxxxxxxxx','xxxxxxxxxxxxxxxxxxxxxxx')

auth.set_access_token('xxxxxxxxxxx-xxxxxxxxxxxxx','xxxxxxxxxxxxxxxxxxxxxxxxx')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

   

search_results = api.search(q="#KisanMajdoorEktaZindabaad", count=10)
for tweet in search_results:
    try:
        status = api.get_status(tweet.id) 
        isfavorited = status.favorited
        isretweeted = status.retweeted
        # print(isretweeted) 
        if isfavorited == True:  
            print('you already liked')
            
        else:
            tweet.favorite()
            print('Tweet Liked ')
            time.sleep(1)
        
        if isretweeted == True:
            print('Tweet already retweeted')
        else:
            tweet.retweet()
            print('retweeted done')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break




f = open("noStatus.txt", "r")
num = int(f.read())
f.close()
for x in range(num,num+2):
    try:
        mystatus = ("#KisanMajdoorEktaZindabaad\n#FarmersProtest"+str(x))
        api.update_status(mystatus)
        time.sleep(1)
    except tweepy.TweepError as e:
        print(e.reason)
f = open("noStatus.txt", "w")
f.write(str(num+2))
f.close()



userID = 'diljitdosanjh'
tweets = api.user_timeline(screen_name=userID, 
                           count=2,
                           include_rts = False,
                           tweet_mode = 'extended'
                           )
f = open("lastid.txt", "r")
data = f.read()
f.close()
for info in tweets[:1]:
    dilid = info.id
    print("\n")
    if  int(data) == int(dilid):
        print('you already retweeted')
    else:
        api.retweet(dilid)
        info.favorite()
        api.update_status(status = '#KisanMajdoorEktaZindabaad\n#FarmersProtest', in_reply_to_status_id = dilid , auto_populate_reply_metadata=True)
        print('liked retweeted replyed')
        f = open("lastid.txt", "w")
        f.write(str(dilid))
        f.close()