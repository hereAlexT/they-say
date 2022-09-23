from data_preparation.data_processing.Processing import Processing
import data_preparation.config
import spacy
from collections import Counter
import re
from emoji import EMOJI_DATA


class WordFrequencyEngine(Processing):
    def __init__(self):
        super().__init__()

    @staticmethod
    def rough_tokenization(text):
        freq_dict = {}
        words = text.split(" ")
        for w in words:

            # remove invlaid char
            w = w.lower()
            for c in w:
                if c not in config.VALID_CHAR:
                    w = w.replace(c, "")

            if w in freq_dict:
                freq_dict[w] += 1
            else:
                freq_dict[w] = 1
        return freq_dict

    @staticmethod
    def spacy_tokenization(text):
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 999999999999
        doc = nlp(text)
        words = []
        for token in doc:
            if token.is_punct is False:
                if token.is_stop is False:
                    words.append(token.lemma_.lower())
        return words

    @staticmethod
    def count_freq(words_list):
        word_freq = Counter(words_list)
        return word_freq

    @staticmethod
    def get_at_n_hash(text):
        re_at = "(?<=^|(?<=[^a-zA-Z0-9-_\.]))(@[A-Za-z]+[A-Za-z0-9-_]+)"
        hash_at = "\s([#][\w_-]+)"
        at_l = re.findall(re_at, text)
        hash_l = re.findall(hash_at, text)

        emoji_l = []
        for i in text:
            if i in EMOJI_DATA:
                emoji_l.append(i)

        return at_l, hash_l, emoji_l
