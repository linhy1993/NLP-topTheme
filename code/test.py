
import gensim

print("[INFO] word2vec model is loading ...")
model = gensim.models.KeyedVectors.load_word2vec_format('word2vec_model.bin', binary=True)
print("[INFO] word2vec model has been loaded.")


b = ['word']
c = ['sentence']
a = model.similarity(b[0], c[0])

print(a)