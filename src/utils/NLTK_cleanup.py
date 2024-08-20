import nltk
import nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import unicodedata # Handle accents

#Download Neccessary NLTK data files
class NLTKprocessing:
    def __init__(self, language: str = 'en') -> None:
        self.stop_words = set(stopwords(language))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
    
# Tokenization
# Break down sentences into words
    def tokenize(self, text):
        """
            Tokenize sentences into list of words
        """
        return word_tokenize(text)

# Stop Word Removal
# words like "and", "the"
    def remove_stopwords(self, text):
        return [word for word in self.stop_words if word.lower() not in self.stop_words]


# Stemming and Lemmatization
    def stem(self, words):
        """
        Apply stemming to reduce words to their root form
        """
        return [self.stemmer.stem(word) for word in words]


    def lemmatization(self, words):

        return [self.lemmatizer.lemmatize(word) for word in words]

# Lower case
# Alter capitalised letters


    def to_lower(self, words):
        return [word.lower() for word in words]


def preprocess(self, text):
        """
        Full preprocessing pipeline: tokenization, stopword removal, 
        lowercasing, stemming, and lemmatization.
        """
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        tokens = self.to_lower(tokens)
        tokens_stemmed = self.stem(tokens)
        tokens_lemmatized = self.lemmatize(tokens)
        
        return {
            'tokens': tokens,
            'tokens_stemmed': tokens_stemmed,
            'tokens_lemmatized': tokens_lemmatized
        }

