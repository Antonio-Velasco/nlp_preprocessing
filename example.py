from utils import CleanDuplicated, CleanSpaces, OnlyAlphanumeric
from utils import LowerCase, Nums2Words

## Examples on how to use the modular functions

def Clean_Raw_text(text: str) -> str:
    text = CleanDuplicated(text)
    text = LowerCase(text)
    text = CleanSpaces(text)
    text = OnlyAlphanumeric(text)
    text = Nums2Words(text)
    text = CleanDuplicated(text)
    return text

def Clean_Cognitive_Search_Content(text: str) -> str: 
    text = ' '.join([t for t in text.split('\n') if len(t.split(' '))>1 and len(t)>3]) 
    text = CleanDuplicated(text) 
    text = OnlyAlphanumeric(text) 
    text = CleanSpaces(text) 
    text = CleanDuplicated(text) 
    return text