streaming.py -- get tweets which has "$AAPL" 
auth.py -- authentication details

ImportAppleTweets.sh -- Import Tweets to Tweets DataBase ; Collection Name is AppleTweets

FilterTweets.py  -- Filter only Tweets from selected Sources ; create new collection FilterAppleTweets

ScoreTweets.py -- Creates a file Score.txt with fileds time and normalized score
Plot.py -- Plot the output


Job.sh
ImportAppleTweets.sh 
FilterTweets.py  
ScoreTweets.py
Plot.py


Run One time

ImportCorpus.sh  -- Import Corpus to Tweets DataBase ; Collection Name is Corpus
db.FilterAppleTweets.ensureIndex({ text:"text"}) -- Create Index 

