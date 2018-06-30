from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


wnl = WordNetLemmatizer()

word_tokened = word_tokenize('He')

pos = pos_tag(["he"])
print(pos[0][1])
# for word in word_tokened:
#     print(wnl.lemmatize(word, pos='n'))
