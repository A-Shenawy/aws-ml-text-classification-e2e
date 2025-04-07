import pandas as pd
import numpy as np
import html
import unicodedata
import re
import string
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import s3fs

# Download NLTK dependencies
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer





# Load data
dataset = pd.read_csv('s3://shenawy-ml-text/IMDB Dataset.csv')
df = dataset.head(100)


stop_words = set(stopwords.words('english'))

def remove_special_chars(text):
    re1 = re.compile(r'  +')
    x1 = text.lower().replace('#39;', "'").replace('amp;', '&').replace('#146;', "'") \
            .replace('nbsp;', ' ').replace('#36;', '$').replace('\\n', "\n") \
            .replace('quot;', "'").replace('<br />', "\n").replace('\\"', '"') \
            .replace('<unk>', 'u_n').replace(' @.@ ', '.').replace(' @-@ ', '-') \
            .replace('\\', ' \\ ')
    return re1.sub(' ', html.unescape(x1))

def remove_non_ascii(text):
    return unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode('utf-8','ignore')

def to_lowercase(text):
    return text.lower()

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def replace_numbers(text):
    return re.sub(r'\d+', '', text)

def text2words(text):
    return word_tokenize(text)

def remove_stopwords(words):
    return [word for word in words if word not in stop_words]

def lemmatize_words(words):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words]

def normalize_text(text):
    """Applies all preprocessing steps to text"""
    text = remove_special_chars(text)
    text = remove_non_ascii(text)
    text = remove_punctuation(text)
    text = to_lowercase(text)
    text = replace_numbers(text)
    words = text2words(text)
    words = remove_stopwords(words)
    words = lemmatize_words(words)
    return ' '.join(words)

# Apply the complete pipeline
df['cleaned_review'] = df['review'].apply(normalize_text)

print("\nCleaned Data Sample:")
print(df[['review','cleaned_review']].head())