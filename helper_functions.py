import string
import re

#Helper Functions
def clean_text(text,lowercase=False):
    
    corpus =  text

    punc = string.punctuation.replace("-","")
    
    if lowercase:
        corpus = text.lower()

    translator = str.maketrans(" "," ",punc)
    
    clean_corpus = corpus.translate(translator)
    
    remove_extra_whitespaces = [token.strip() for token in clean_corpus.split()]

    return " ".join(remove_extra_whitespaces)


#https://stackoverflow.com/questions/38291313/split-list-from-text-into-ngrams-in-python
def ngrams(text, n):
    words = text.split()
    return [ words[i:i+n] for i in range(len(words))]

def remove_text_in_parens(text, replace_with="", space_before=True):
    """Return string of provided text with any text within parenthesis replaced with given replace_with value, default ''.
    
    If space_before is True, will also check for the space before the parenthesis and remove that.
    This helps prevent some erroneous double spaces from being entered into the text.
    """
    
    # This pattern removes all characters contained within parenthesis:
    # Ex. (This was demonstrated in Blah Blah 2018...) --> replace_with
    if space_before:
        pattern = re.compile(r'\s\((.*?)\)')
    
    else:
        pattern = re.compile(r'\((.*?)\)')
    
    # Make sure the input text is a string, otherwise it won't work with df.apply:
    text_string = str(text)
    
    clean_text = pattern.sub(replace_with, text_string)
    
    return clean_text