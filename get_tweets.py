from twython import Twython # pip install twython
import time # standard lib

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'a2bLpVe5RKCp3miLncRSJj4uv'
CONSUMER_SECRET = 'eokqscaZnUuulyHPbhT4HUdfikiWARV9yOiyp1K5BVw5anDeHR'
ACCESS_KEY = '1395752780-GVCvpoVgCmyrhLKknaIyICwH9bDETpUem2JQ9HC'
ACCESS_SECRET = '3kn6YVXULEy5HGsG7EuwcROuIWKH2fUeSMOiQ6f3l4o4z'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
lis = [467020906049835008] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="kanyewest",
    count=200, include_retweets=False, max_id=lis[-1])
    time.sleep(300) ## 5 minute rest between api calls

    for tweet in user_timeline:
        print tweet['text'] ## print the tweet
        lis.append(tweet['id']) ## append tweet id's