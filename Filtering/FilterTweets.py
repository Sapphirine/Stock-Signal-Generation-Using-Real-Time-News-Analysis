from pymongo import MongoClient
client = MongoClient()
db = client.Tweets
cursor = db.AppleTweet.find({"user.screen_name": {'$in':[
"Seeking Alpha","Trefis.com","Barron's","Bloomberg News","MarketWatch","TechCrunch","BBC Technology","Wall Street Journal","Financial Times"]}},{'_id' : 0, 'text' : 1, 'user.screen_name' : 1})
for doc in cursor:
    db.FilterAppleTweets.insert(doc)
