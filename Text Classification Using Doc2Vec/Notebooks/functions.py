import demoji
import re
import requests
import nltk
demoji.download_codes()
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import words
from gensim.models.doc2vec import TaggedDocument




# preprocessing function. To remove RTs, handle names and hashtags along with text
def data_cleaner(column):
    column = column.apply(lambda x: demoji.replace(str(x),''))
    column = column.apply(lambda x:re.sub('RT @[\w_]+: ', ' ',str(x)))
    return column

# preprocessing function. To remove RTs, handle names and hashtags along with text
def data_cleaner_tweets(column):
    pattern = re.compile('RT @[\w_]+: |https?:\/\/.*[\r\n]*|[^A-Za-z0-9]+')
    column = column.apply(lambda x: demoji.replace(str(x),''))
    column = column.apply(lambda x:re.sub(pattern, ' ',str(x)))
    #column = column.str.lower()
    #column = column.str.strip()
    #column = column.apply(lambda x:re.sub('[^A-Za-z0-9]+',' ',x))
    #column = column.apply(lambda x:re.sub('[^A-Za-z0-9]+',' ',x))
    return column

def tokenize_text(text):
    tokens = []
    for sent in nltk.sent_tokenize(text):
        for word in nltk.word_tokenize(sent):
            if len(word) < 2:
                continue
            tokens.append(word.lower())
    return tokens


def vector_for_learning(model, input_docs):
    sents = input_docs
    targets, feature_vectors = zip(*[(doc.tags[0], model.infer_vector(doc.words, steps=20)) for doc in sents])
    return targets, feature_vectors

def word_lem(word_list):
    lemma = WordNetLemmatizer()
    return [lemma.lemmatize(word) for word in word_list]

#English lang cleaner
def is_english(word_list):
    cleaned = []
    for word in word_list:
        if word in words.words():
            cleaned.append(word)
    return cleaned

#Creating TaggedDocuments
def f_docbuilder(x,y):
    for i in range(len(x)):
        dataset.append(TaggedDocument(words=x[i], tags=[y[i]] ))