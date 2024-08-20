import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import string

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def preprocess(self, text):
        # Tokenize sentences
        sentences = sent_tokenize(text)
        
        # Tokenize words and remove stopwords and punctuation
        processed_sentences = []
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            words = [self.stemmer.stem(word) for word in words if word not in self.stop_words and word not in string.punctuation]
            processed_sentences.append(' '.join(words))
        
        return sentences, processed_sentences
