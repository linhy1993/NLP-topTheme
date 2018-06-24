from top_theme import TopTheme
from func import language_regonize


if __name__ == '__main__':
    top_theme_obj = TopTheme();
    top_theme_obj.set_language_regonizer(language_regonize);
    top_theme_obj.set_sentence_tokenizer(sentence_tokenize)
    top_theme_obj.theme_cluster(theme_cluster)
    top_theme_obj.set_indexer(indexer)
    top_theme_obj.set_phrase_extractor(phrases_extract)
    top_theme_obj.build()
