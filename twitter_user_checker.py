import tweepy
from datetime import datetime, timedelta

# Enter consumer_key, consumer_secret, access_token_key, and access_token_secret below
consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token_key, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

#Get twitter handles
print("Enter 5 twitter handles :")
tweeters_list = []
for i in range(0, 5):
    t = input()
    tweeters_list.append(t)

startDate = datetime.now() - timedelta(hours = 24)

#tweeters who have interacted in last 24 hours
tweeters = []

for tweeter in tweeters_list:
    tmpTweets = api.user_timeline(tweeter)
    for tweet in tmpTweets:
        if tweet.created_at > startDate:
            tweeters.append(tweeter)
        break

print("\n\n")
print("Users interacted with their tweets in last 24 hours are :\n")
if(len(tweeters) == 0):
    print("None")
else:
    for t in tweeters:
        print(t)