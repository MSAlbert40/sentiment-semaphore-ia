import re

def preprocessText(sen):
    '''
    Method to delete not necessary characters and words
    '''
    #Remove @ words
    sen = ' '.join(word for word in sen.split(' ') if not word.startswith('@'))
    
    # Removing html tags
    sentence = removeTags(sen)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Záéíóúñ]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence


TAG_RE = re.compile(r'<[^>]+>')

def removeTags(text):
    '''
    Method to remove all html tags
    '''
    return TAG_RE.sub('', text)

def removeStopwords(tokens, stoplist): 
    '''
    Remove all the stopwords from tokens using a stopwords list
    '''
    return [word for word in tokens if word not in stoplist]

def lowerToken(tokens): 
    '''
    Put all tokens into lowercase
    '''
    return [w.lower() for w in tokens]  