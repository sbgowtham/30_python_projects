from textblob import TextBlob

text = "you are a bad person"
analysis = TextBlob(text)
sentiment = analysis.sentiment.polarity

if sentiment > 0:
    print("Positive sentiment")
elif sentiment < 0:
    print("Negative sentiment")
else:
    print( "Neutral sentiment")