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
    clean_txt = clean(text, no_emoji=True)
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
    # model2 = load_model("../MLmodel/model2.h5")

    print("8")
    result = model1.predict(sample_padded)[0][0]
    print(result)
    f_res = ""
    if result < 0.5:
        f_res = "HOF"
    else:
        f_res = "NOT"

    return f_res


sample = "hate wen females hit ah nigga with tht bro Im tryna make u my la sweety fuck ah bro"

print(prepros(sample))

