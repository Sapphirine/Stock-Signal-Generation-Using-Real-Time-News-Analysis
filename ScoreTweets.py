from decimal import *
from datetime import datetime
from pymongo import MongoClient
client = MongoClient()
db = client.Tweets
arr = list(db.Corpus.find())
cnt = 0
word_score = 0
tot_score = 0
length = len(arr)
for i in range(0,length):
  print(  arr[i])
  newdict = arr[i]
  searchword = newdict['Word']
  score = newdict['Score']
  print(searchword)
  print(score)
  cnt =  db.FilterAppleTweets.find( { '$text': {'$search': searchword } } ).count()
  print("cnt" , cnt)
  if cnt > 0:
    tot_score +=  score


print(" total score " , tot_score)
print(" total tweets " , length)
norm_score = Decimal(tot_score)/Decimal(length)
print(" Norm  score " , norm_score)
time = str(datetime.now())
file = open("Score.txt", "ab")
file.write(time+','+str(norm_score)+"\n")
file.close()
