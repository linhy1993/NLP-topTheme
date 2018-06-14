class TopTheme:
    """docstring for TopTheme."""

    def __init__(self):
        self.language_regonizer = 0
        self.sentence_tokenizer = 0
        self.theme_cluster = 0

    def set_language_regonizer(language_regonizer):
        self.language_regonizer = language_regonizer


    def set_sentence_tokenizer(sentence_tokenizer):
        self.sentence_tokenizer = sentence_tokenizer


    def set_theme_cluster(theme_cluster):
        self.theme_cluster = theme_cluster


    def get_top_theme():
        if self.set_language_regonizer == 0:
            print("ERROR: language_regonizer never setted")
            pass
        if self.sentence_tokenizer == 0:
            print("ERROR: sentence_tokenizer never setted")
            pass
        if self.theme_cluster == 0:
            print("ERROR: theme_cluster never setted")
            pass

        




















if __name__ == '__main__':
