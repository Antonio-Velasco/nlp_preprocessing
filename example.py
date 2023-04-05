from utils import cleanduplicated, cleanspaces, onlyalphanumeric
from utils import lowercase, nums2words

## Examples on how to use the modular functions

def cleantext(text: str) -> str:
    text = CleanDuplicated(text)
    text = LowerCase(text)
    text = CleanSpaces(text)
    text = OnlyAlphanumeric(text)
    text = Nums2Words(text)
    text = CleanDuplicated(text)
    return text

def clean_cognitive_search_content(text: str) -> str: 
    text = ' '.join([t for t in text.split('\n') if len(t.split(' '))>1 and len(t)>3]) 
    text = CleanDuplicated(text) 
    text = OnlyAlphanumeric(text) 
    text = CleanSpaces(text) 
    text = CleanDuplicated(text) 
    return text
