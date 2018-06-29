import numpy as np
import nltk
import gensim
import re
from stop_words import get_stop_words
import nltk
import scipy as sc
import numpy as np
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)


def phrases2vec(phrases):
    vectorSet = []
    for aword in phrases:
        try:
            wordVector = model.wv[aword]
            vectorSet.append(wordVector)
        except:
            pass
    phrases2vec_value = np.divide(vectorSet,len(phrases))
    return phrases2vec_value

if __name__ == '__main__':
    phrases_vec = phrases2vec(['hello','good'])
    print(phrases_vec)