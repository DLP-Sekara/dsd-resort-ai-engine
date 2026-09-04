import pickle
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class NLPAnalyzer:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, '../static/model/dsd_nlp_sentiment_model.pickle')
        vectorizer_path = os.path.join(base_dir, '../static/model/dsd_nlp_vectorizer.pickle')
        
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
            
        with open(vectorizer_path, 'rb') as f:
            self.vectorizer = pickle.load(f)
            
        self.ps = PorterStemmer()
        self.all_stopwords = set(stopwords.words('english'))
        if 'not' in self.all_stopwords:
            self.all_stopwords.remove('not')

    def analyze(self, text: str):
        review = re.sub('[^a-zA-Z]', ' ', text)
        review = review.lower()
        review = review.split()
        review = [self.ps.stem(word) for word in review if not word in self.all_stopwords]
        clean_text = ' '.join(review)
        
        text_vector = self.vectorizer.transform([clean_text]).toarray()
        
        prediction = self.model.predict(text_vector)[0] # 1 (Positive) or 0 (Negative)
        probabilities = self.model.predict_proba(text_vector)[0]
        
        confidence = round(max(probabilities) * 100, 2)
        sentiment_label = "Positive" if prediction == 1 else "Negative"
        
        return sentiment_label, confidence