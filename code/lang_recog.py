import nltk
import pickle
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.punkt import PunktSentenceTokenizer


def language_regonize(text):
    """
    return the language of *text*,
    regonize the language by checking whether stopwords in specific language is included in text or not
    language supported : english, french
    :param text: text that includes only one language
    :type text: str
    """
    lang_freq = {}
    support_language = ['english','french']
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]
    for lang in support_language:
        stopwords_set = set(stopwords.words(lang))
        words_set = set(words)
        common_ele = words_set.intersection(stopwords_set)
        lang_freq[lang] = len(common_ele)

    return max(lang_freq, key=lang_freq.get)


def sentence_tokenize(text, language='english'):
    """
    return an array that includes tokenized sentences of *text*,
    use nltk.PunktSentenceTokenizer to tokenize sentence
    language supported : english, french
    :param text: whole paragraphs of single-language text
    :type text: str
    :param language: the language of the text
    :type language: str
    """
    sentence_arr = {}
    if language == 'english':
        sentence_arr = sent_tokenize(text, language='english')
    elif language == 'french':
        sentence_arr = sent_tokenize(text, language='french')
    else:
        print('ERROR:language inputed is out of support in sentence_tokenize()')

    return sentence_arr


def theme_cluster(words_arr):
    """

    language supported : english, french
    :param words_arr:
    :type words_arr: array of str
    """
    



if __name__ == '__main__':
