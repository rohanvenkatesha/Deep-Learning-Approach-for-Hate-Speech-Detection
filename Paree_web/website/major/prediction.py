from keras.models import load_model
import string
from nltk.corpus import stopwords
import re
import nltk
from nltk.tokenize import WhitespaceTokenizer
from cleantext import clean
from tensorflow.keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer
import pickle
import numpy as np
import emoji


def remove_punctuation(text):
    print("1")
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree


tk = WhitespaceTokenizer()
def tokenization(text):
    print("2")
    return tk.tokenize(text)

import nltk
#Stop words present in the library
stopwords = nltk.corpus.stopwords.words('english')
 
#defining the function to remove stopwords from tokenized text
def remove_stopwords(text):
    print("3")
    output= [i for i in text if i not in stopwords]
    return output


def rem_em(text):
    print("4")
    clean_txt = clean(text, fix_unicode=True)
    return clean_txt



def prepros(sample):
    max_len = 34
    print("6")
    sample = sample.lower()
    print(sample)
    sample = remove_punctuation(sample)
    print(sample)
    sample = tokenization(sample)
    print(sample)
    sample = remove_stopwords(sample)
    print(sample)
    sample = rem_em(sample)
    # loading
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    sample_sequences = tokenizer.texts_to_sequences([sample])
    sample_padded = pad_sequences (sample_sequences, maxlen = max_len, padding = 'post', truncating = 'post' )

    print("7")
    model1 = load_model("model1.h5")
    model2 = load_model("model2.h5")

    print("8")
    result1 = model1.predict(sample_padded)[0][0]
    result2 = model2.predict(sample_padded)

    f_res = ""
    if result1 < 0.5:
        f_res = "HOF"
    else:
        f_res = "NOT"

    val = np.argmax(result2, axis = 1)[0]

    if val == 0:
        f_res = f_res+" -> HATE"
    elif val == 1:
        f_res = f_res+" -> NONE"
    elif val == 2:
        f_res = f_res+" -> OFFN"
    else :
        f_res = f_res+" -> PRFN"

    return f_res


# sample = "Hello How are you I am fine here have a good day"

# print(prepros(sample))

