import os
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from data import save_pickle
from data import read_pickle
from data import str_of


class TopTheme:
    """docstring for TopTheme."""

    def __init__(self):
        self.language_regonizer = 0
        self.sentence_tokenizer = 0
        self.theme_cluster = 0
        self.indexer = 0

    def set_language_regonizer(language_regonizer):
        self.language_regonizer = language_regonizer


    def set_sentence_tokenizer(sentence_tokenizer):
        self.sentence_tokenizer = sentence_tokenizer


    def set_theme_cluster(theme_cluster):
        self.theme_cluster = theme_cluster

    def set_indexer(indexer):
        self.indexer = indexer


    def build(folder_path):
        if isinstance(self.language_regonizer, function):
            print("ERROR: language_regonizer never setted or type error")
            pass
        if isinstance(self.sentence_tokenizer, function):
            print("ERROR: sentence_tokenizer never setted")
            pass
        if isinstance(self.theme_cluster, function):
            print("ERROR: theme_cluster never setted")
            pass
        if isinstance(self.indexer, function):
            print("ERROR: theme_cluster never setted")
            pass

        sentence_index = -1
        for file_name in os.listdir(folder_path):
            doc = read_txt(folder_path + file_name)
            print("INFO: reading " + file_name + "to build TopTheme model")
            # spilit doc to paragraphs, suppose single language in one paragraph
            paragraphs = doc.split('\r\n')
            for parag in paragraphs:
                language = self.language_regonizer(parag)
                # sentence tokenize
                lst_sentence = self.sentence_tokenizer(parag, language)
                for sentence in lst_sentence:
                    sentence_index += 1
                    # remove all punctuation
                    removed_punc = ''.join(s for s in sentence if s not in punctuations)
                    # remove all digits
                    removed_digit = re.sub(r'\d+', '', removed_punc)
                    # case fold
                    after_case_fold = removed_digit.lower()
                    # tokenize
                    word_tokens = nltk.word_tokenize(after_case_fold)
                    # filter stop words
                    removed_stopwords = [t for t in word_tokens if t not in stopwords.words(language)]
                    # stemming
                    for t in removed_stopwords:
                        token = porter_stemmer.stem(t)
                        print(token)
