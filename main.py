from textblob import TextBlob

class SentimentAnalyzer:

    def __init__(self, text):
        self.text = text

    def analyze_sentiment(self):
        analysis = TextBlob(self.text)

        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity < 0:
            return "Negative"
        else:
            return "Neutral"


user_text = input("Enter a sentence: ")

analyzer = SentimentAnalyzer(user_text)

result = analyzer.analyze_sentiment()

print("Sentiment:", result)