from flask import Flask, render_template, request
import re
import joblib
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('models/model.joblib')
vectorizer = joblib.load('models/vectorizer.joblib')

# Define a function to preprocess the input text
def clean_text(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # Remove mentions
    text = re.sub(r'https?:\/\/\S+', '', text)  # Remove hyperlinks
    text = re.sub(r'#', '', text)  # Remove hashtags
    text = re.sub(r'RT', '', text)  # Remove retweets
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    return text

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the input text from the form
        tweet = request.form['tweet']
        
        # Preprocess the input text
        tweet_clean = clean_text(tweet)
        tweet_vec = vectorizer.transform([tweet_clean])
        
        # Predict the sentiment of the tweet
        sentiment = model.predict(tweet_vec)[0]
        
        # Return the prediction to the web page
        if sentiment == 0:
            return render_template('home.html', sentiment='Negative')
        else:
            return render_template('home.html', sentiment='Positive')
    
    # Render the web page
    return render_template('home.html', sentiment='')

if __name__ == '__main__':
    app.run(debug=True)
