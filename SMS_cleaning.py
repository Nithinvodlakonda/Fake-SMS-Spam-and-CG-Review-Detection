# SMS_cleaning.py
import string
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_SMS(text):
    # - Converts text to lowercase
    text = text.lower()  
    # Remove digits
    text = re.sub(r'\d+', '', text)
    # - Removes punctuation and digits
    text = text.translate(str.maketrans('', '', string.punctuation))  
    # - Strips leading/trailing spaces
    text = text.strip() 
    # - Tokenizes and removes stopwords 
    words = text.split()
    # - Applies stemming using PorterStemmer
    words = [ps.stem(word) for word in words if word not in stop_words]  
    return " ".join(words)
