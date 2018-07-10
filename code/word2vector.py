import gensim

print("[INFO] word2vec model is loading ...")
model = gensim.models.KeyedVectors.load_word2vec_format('word2vec_model.bin', binary=True)
print("[INFO] word2vec model has been loaded.")


def word2vector(word):
    """
    input a word and obatin the vector of the word
    :param word:
    :type str
    :return: word's vector
    :type list
    """
    word_vec = []
    try:
        word_vec = model.wv[word]

    except KeyError:
        print("[WARNING] fail to obtain vector of (" + word + "), not found in vocabulary")
    return word_vec

def TwoWordsSimilarity(wordlist1, wordlist2):
    """
    compare two words similarity
    
    :param wordlist1: clustered word
    :param wordlist2: question word
    :return: similarity, value from 0 to 1
    :type: float
    """
    word_similarity = model.similarity('woman', 'man')
    return word_similarity





if __name__ == '__main__':
    words_list = ['personal', 'important']
    for w in words_list:
        print("----- " + w +" -----")
        vec = word2vector(w)
        print(vec)
        print("len of vector:" + str(len(vec)))
