
# import goslate
# gs = goslate.Goslate()
#
# list = gs.translate("X##connaît##tres##bien##son##métier##mais##montre##quand##même##une##ouverture##aux##idées##des##autres.##Il##est##très##professionnelet##prends##toujours##en##Compte", 'en')
# list = str(list).split('##')
# print(list)








# import nltk
# a = nltk.edit_distance("leader", "collaborator")
# print(a)
#
# import gensim
#
# print("[INFO] word2vec model is loading ...")
# model = gensim.models.KeyedVectors.load_word2vec_format('word2vec_model.bin', binary=True)
# print("[INFO] word2vec model has been loaded.")
#
# b = model.similarity('leader', 'collaborator')
#
# print(b)

#
#
#
#
# lst_tokens_fr_after = "generosity#knowledge#passionnate#understand#collaborative"
# lst_tokens_fr_final = []
# lst_tokens_fr_final = lst_tokens_fr_after.split('#')
#
#
# print(lst_tokens_fr_final)
#
#
# for token in lst_tokens_fr_final:
#     print(token)
#
#
# from translate import Translator
# translator= Translator(to_lang="zh")
# translation = translator.translate("This is a pen.")
# print(translation)

# from googletrans import Translator
# translator = Translator()
# lst = translator.translate('generosity#knowledge#passionnate#understand#collaborative',dest='fr')
# print(lst.text)
#
# import pymongo
# from pymongo import MongoClient
#
# uri = "mongodb://top-theme-mongo:L4SDrxH8M7jk9Z7iotMcx6FxOPLaF6CWkF2ZfUhQKiAK5zN3KqFkQFNVLCsyGNTGapk0RGLZD1YiIuVLQRoC5w==@top-theme-mongo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
# client = pymongo.MongoClient(uri)
# db = client.test    #Select the database
# collection = db.test_collection
#
#
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"]}






