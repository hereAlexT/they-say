import data_preparation.secret_env as secret_env


class Processing:
    def __init__(self):
        self.spacy_model = secret_env.SPACY_MODEL

    def get_spacy_model(self):
        return self.spacy_model
