import os
import sys
import nltk
from types import FunctionType
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from data import save_pickle
from data import read_pickle
from data import save_txt
from data import read_txt
from data import str_of

IF_DEBUG = True

class TopTheme:
    """docstring for TopTheme."""

    def __init__(self):
        self.language_regonizer = 0
        self.sentence_tokenizer = 0
        self.theme_cluster = 0
        self.indexer = 0
        self.phrase_extractor = 0

    def set_language_regonizer(self, language_regonizer):
        self.language_regonizer = language_regonizer


    def set_sentence_tokenizer(self, sentence_tokenizer):
        self.sentence_tokenizer = sentence_tokenizer


    def set_theme_cluster(self, theme_cluster):
        self.theme_cluster = theme_cluster

    def set_indexer(self, indexer):
        self.indexer = indexer

    def set_phrase_extractor(self, phrase_extractor):
        self.phrase_extractor = phrase_extractor


    def build(self, folder_path):
        if not isinstance(self.language_regonizer, FunctionType):
            print("ERROR: language_regonizer never setted or type error")
            return 0
        if not isinstance(self.sentence_tokenizer, FunctionType):
            print("ERROR: sentence_tokenizer never setted")
            return 0
        if not isinstance(self.theme_cluster, FunctionType):
            print("ERROR: theme_cluster never setted")
            return 0
        if not isinstance(self.indexer, FunctionType):
            print("ERROR: indexer never setted")
            return 0
        if not isinstance(self.phrase_extractor, FunctionType):
            print("ERROR: phrase_extractor never setted")
            return 0

        sentence_index = -1
        sentences_store = []
        inversed_index = {}

        for file_name in os.listdir(folder_path):
            doc = read_txt(folder_path + '/' + file_name)
            print("INFO: reading " + file_name + "to build TopTheme model")
            # spilit doc to paragraphs, suppose single language in one paragraph
            paragraphs = doc.split('\r\n')
            for parag in paragraphs:
                language = self.language_regonizer(parag)
                if(language == 'french'):
                    continue
                # sentence tokenize
                lst_sentence = self.sentence_tokenizer(parag, language)
                # save original sentence to memory
                sentences_store.append(lst_sentence)

                for sentence in lst_sentence:
                    sentence_index += 1
                    # case fold
                    sentence = sentence.lower()
                    # extract phrases
                    phrases = self.phrase_extractor(sentence)
                    # remove these phrases from sentence
                    for p in phrases:
                        sentence = sentence.replace(p, '')

                    # remove all punctuation
                    removed_punc = ''.join(s for s in sentence if s not in punctuations)
                    # remove all digits
                    removed_digit = re.sub(r'\d+', '', removed_punc)
                    # tokenize
                    word_tokens = nltk.word_tokenize(removed_digit)
                    # filter stop words
                    removed_stopwords = [t for t in word_tokens if t not in stopwords.words(language)]
                    # stemming
                    for t in removed_stopwords:
                        token = porter_stemmer.stem(t)
                        # index
                        self.indexer(token, sentence_index, inversed_index)
        # persist the index
        save_pickle(inversed_index, 'out.pickle')
        save_txt(str_of(inversed_index), 'out.txt')
