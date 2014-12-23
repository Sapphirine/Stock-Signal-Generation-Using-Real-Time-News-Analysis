This is the code submitted for Project ID: 201412-6 
Team:
Rajesh Madala
Shreyas Shrivastava
Mayank Misra
Mandeep Singh

Below is a short description of the files:

streaming.py -- get tweets which has "$AAPL" 
auth.py -- authentication details

ImportAppleTweets.sh -- Import Tweets to Tweets DataBase ; Collection Name is AppleTweets

FilterTweets.py  -- Filter only Tweets from selected Sources ; create new collection FilterAppleTweets

ScoreTweets.py -- Creates a file Score.txt with fileds time and normalized score


Job.sh
ImportAppleTweets.sh 
FilterTweets.py  
ScoreTweets.py

Run One time

ImportCorpus.sh  -- Import Corpus to Tweets DataBase ; Collection Name is Corpus
db.FilterAppleTweets.ensureIndex({ text:"text"}) -- Create Index 

