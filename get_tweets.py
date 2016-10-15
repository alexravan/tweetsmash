from twython import Twython, TwythonError # pip install twython
import time # standard lib
import csv
import sys

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'ZBxlzgXKatHdHRyhjapkzrCwn'
CONSUMER_SECRET = 'EpK11g1aQ3uHPZAhfkDSX0tPfGAvgiqgpBBXSD63cjC3AovFQO'
ACCESS_KEY = '112619837-oYa5yIMFeuA3VvNRudFQDdyuavB4PX8OPkvAvhgj'
ACCESS_SECRET = 'VIUxuIhltjeeZOPez8b9U3L5WQDIBJWMwFIlfNECRyCUj'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

lis = [467020906049835008] ## this is the latest starting tweet id
filepath = "tweets/" + sys.argv[2]
calls = 1

for i in range(0, 16): ## iterate through all tweets
	f = open(filepath, 'a')
## tweet extract method with the last list item as the max_id
#     user_timeline = twitter.get_user_timeline(screen_name="sys.argv[1]",
#     count=200, include_retweets=False, max_id=lis[-1])
	try:
	    user_timeline = twitter.get_user_timeline(screen_name=sys.argv[1], count=200, include_retweets=False, max_id=lis[-1])
	except TwythonError as e:
	   print e

	try:
	    writer = csv.writer(f)
	    for tweet in user_timeline:
			writer.writerow( [tweet['text'].encode('utf-8')] )	
			lis.append(tweet['id'])
	finally:
		f.close()
	# if calls == 5:
	print "==================sleeping=================="
	time.sleep(300)
	print "==================done sleeping=================="

		# calls = 0
	# else:
		# calls += 1



    # for tweet in user_timeline:

#         # print tweet['text'] ## print the tweet
#         lis.append(tweet['id']) ## append tweet id's
# try:
#     user_timeline = twitter.get_user_timeline(screen_name=sys.argv[1], count=3000)
# except TwythonError as e:
#    print e

# # filepath = "tweets/" + sys.argv[2]
# # f = open(filepath, 'wt')
# try:
#     writer = csv.writer(f)
#     for tweets in user_timeline:
# 		writer.writerow( [tweets['text'].encode('utf-8')] )	
# finally:	
# 	f.close()

