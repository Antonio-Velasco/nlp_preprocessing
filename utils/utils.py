from itertools import chain
import pandas as pd
import re
from num2words import num2words

import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

#Download resources 
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def CleanSpaces(input: str) -> str:
    # Clean multiple empty spaces
    regex = r'(\s\s+)'
    return re.sub(regex, r' ', input, flags=re.IGNORECASE)
    
def CleanDuplicated(input: str) -> str:
    # Matches repeated words and sentences
    regex = r'(\W|^)(.+)\s\2'
    return re.sub(regex, r'\1', input, flags=re.IGNORECASE)
    
def OnlyAlphabetic(input: str) -> str:
    # Matches every non alphabetical character
    regex = '[^a-zA-Z ]'
    return re.sub(regex , " ", input)

def OnlyAlphanumeric(input: str) -> str:
    # Matches every non alphanumerical character
    regex = '[^a-zA-Z1-9 ]'
    return re.sub(regex, " ", input)

def LowerCase(input: str) -> str:
    return input.lower()

def Nums2Words(input: str) -> str:
    regex = ' \d\.?\d* '
    return re.sub(regex, lambda x: ' ' + num2words(x.group()) + ' ', input)

def RemoveStopWords(input: list[str], *args: str) -> list[str]:

    # Removes common English stopwords and custom ones added as *args 
    return [t for t in input if t not in list(chain(*[[*args], stopwords.words('english')]))]

def Lemmatizer(input: list[str]) -> list[str]:

    # Lemmatizes tokens
    return [WordNetLemmatizer().lemmatize(t) for t in input]

def Stemmer(input: list[str]) -> list[str]:

    # Lemmatizes tokens
    return [PorterStemmer().stem(t) for t in input]
