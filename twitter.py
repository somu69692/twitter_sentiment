import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key = 'CONSUMER_KEY_HERE'
consumer_secret = 'CONSUMER_SECRET_HERE'
access_token = 'ACCESS_TOKEN_HERE'
access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'

# Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Step 3 - Retrieve Tweets
search_term = "Trump"  # Change this to any keyword you want to analyze
tweet_count = 100  # Number of tweets to fetch
public_tweets = api.search_tweets(q=search_term, count=tweet_count, lang="en")

# Step 4 - Process Tweets and Save to CSV
# Define sentiment thresholds
positive_threshold = 0.1  # Polarity > 0.1 is Positive
negative_threshold = -0.1  # Polarity < -0.1 is Negative

# File to save analyzed tweets
csv_file = 'tweets_sentiment.csv'

# Open a CSV file to save the results
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Tweet', 'Sentiment', 'Polarity', 'Subjectivity'])
    
    for tweet in public_tweets:
        text = tweet.text  # Get the text of the tweet
        analysis = TextBlob(text)  # Perform sentiment analysis
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity

        # Determine sentiment label
        if polarity > positive_threshold:
            sentiment = 'Positive'
        elif polarity < negative_threshold:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        # Write the tweet data to the CSV file
        writer.writerow([text, sentiment, polarity, subjectivity])

print(f"Tweets have been analyzed and saved to '{csv_file}'.")
