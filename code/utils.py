import re
from itertools import chain

import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer

from num2words import num2words

# ==============================================
# ============  NLP  Processing  ===============
# ==============================================

# Download resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


def cleanspaces(input: str) -> str:
    # Clean multiple empty spaces
    regex = r'(\s\s+)'
    return re.sub(regex, r' ', input, flags=re.IGNORECASE)


def cleanduplicated_words(input: str) -> str:
    # Matches repeated words
    regex = r'\b(\w+)\b\s+\b\1\b'
    return re.sub(regex, r'\1', input, flags=re.IGNORECASE)


def cleanduplicated_sentences(input: str) -> str:
    # Matches repeated words
    regex = r'(?<=\b)([^.!?]+[.!?])\s*\1'
    return re.sub(regex, r'\1', input, flags=re.IGNORECASE)


def onlyalphabetic(input: str, with_space: bool = True) -> str:
    # Matches every non alphabetical character
    regex = '[^a-zA-Z ]'
    if with_space:
        return re.sub(regex, " ", input)
    else:
        return re.sub(regex, "", input)


def onlyalphanumeric(input: str, with_space: bool = True) -> str:
    # Matches every non alphanumerical character
    regex = '[^a-zA-Z1-9 ]'
    if with_space:
        return re.sub(regex, " ", input)
    else:
        return re.sub(regex, "", input)


def lowercase(input: str) -> str:
    # Makes text lowercase
    return input.lower()


def nums2words(input: str) -> str:
    # Replaces numbers with a word equivalent
    regex = '(^|\s)(\d+)(?=\s|[.!?])'  # noqa: W605
    return re.sub(regex, lambda x: ' ' + num2words(x.group()), input)


def removestopwords(input: list[str], *args: str) -> list[str]:
    # Removes common English stopwords and custom ones added as *args
    return [t for t in input if t not in list(
            chain(*[[*args],
                    stopwords.words('english')])
            )]


def lemmatizer(input: list[str]) -> list[str]:
    # Lemmatizes tokens
    return [WordNetLemmatizer().lemmatize(t, pos=wordnet.VERB) for t in input]


def stemmer(input: list[str]) -> list[str]:
    # Lemmatizes tokens
    return [PorterStemmer().stem(t) for t in input]
