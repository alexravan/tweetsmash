from twython import Twython, TwythonError # pip install twython
import time # standard lib
import csv
import sys

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'a2bLpVe5RKCp3miLncRSJj4uv'
CONSUMER_SECRET = 'eokqscaZnUuulyHPbhT4HUdfikiWARV9yOiyp1K5BVw5anDeHR'
ACCESS_KEY = '1395752780-GVCvpoVgCmyrhLKknaIyICwH9bDETpUem2JQ9HC'
ACCESS_SECRET = '3kn6YVXULEy5HGsG7EuwcROuIWKH2fUeSMOiQ6f3l4o4z'

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
	if calls == 5:
		time.sleep(300)
		calls = 0
	else:
		calls += 1
		


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

