import spacy
import pandas as pd
import re


class LanguageProcessing:
    def __init__(self, comment_list):
        self.text = ".".join([comment.text for comment in comment_list])
        self.words = []
        self.nouns = []
        self.adj = []
        self.verbs = []
        self.entities = []
        self.links = []

        self.unwanted = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
                         "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself",
                         "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which",
                         "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be",
                         "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
                         "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
                         "with", "about", "against", "between", "into", "through", "during", "before", "after",
                         "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                         "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
                         "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
                         "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
                         "should", "now"]

    def add_unwanted(self, unwanted_list):
        self.unwanted += unwanted_list
        return self.unwanted

    def extract_keywords(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.text)
        exclude = re.compile('href|\\?|>|<')

        word_list = [token.lemma_ for token in doc if
                     token.lemma_ not in self.unwanted and
                     token.pos_ in ["NOUN", "VERB", "ADJ"]
                     and not exclude.findall(token.lemma_) and len(token.lemma_) > 1]
        noun_list = [token.lemma_ for token in doc if
                     token.lemma_ not in self.unwanted and
                     token.pos_ == "NOUN"
                     and not exclude.findall(token.lemma_) and len(token.lemma_) > 1]
        adj_list = [token.lemma_ for token in doc if
                    token.lemma_ not in self.unwanted and
                    token.pos_ == "ADJ"
                    and not exclude.findall(token.lemma_) and len(token.lemma_) > 1]
        verb_list = [token.lemma_ for token in doc if
                     token.lemma_ not in self.unwanted and
                     token.pos_ == "VERB"
                     and not exclude.findall(token.lemma_) and len(token.lemma_) > 1]
        entity_list = [entity.text for entity in doc.ents
                       if len(entity.text) > 1]
        print(entity_list)
        link_list = [element for element in
                     re.split("\"|'|>|<|\\\\", self.text) if 'https' in element]

        word_names = pd.Series(list(map(lambda word: word.lower(), word_list))).value_counts().index.tolist()
        word_values= pd.Series(list(map(lambda word: word.lower(), word_list))).value_counts().tolist()

        noun_names = pd.Series(list(map(lambda word: word.lower(), noun_list))).value_counts().index.tolist()
        noun_values = pd.Series(list(map(lambda word: word.lower(), noun_list))).value_counts().tolist()

        adj_names = pd.Series(list(map(lambda word: word.lower(), adj_list))).value_counts().index.tolist()
        adj_values = pd.Series(list(map(lambda word: word.lower(), adj_list))).value_counts().tolist()

        verb_names = pd.Series(list(map(lambda word: word.lower(), verb_list))).value_counts().index.tolist()
        verb_values = pd.Series(list(map(lambda word: word.lower(), verb_list))).value_counts().tolist()

        entity_names = pd.Series(list(map(lambda word: word.lower(), entity_list))).value_counts().index.tolist()
        entity_values = pd.Series(list(map(lambda word: word.lower(), entity_list))).value_counts().tolist()

        link_names = pd.Series(link_list).value_counts().index.tolist()
        link_values = pd.Series(link_list).value_counts().tolist()

        self.words = [{"name": word_names[i], "value": word_values[i]}
                      for i in range(len(word_names)) if word_values[i] > 1]
        self.nouns = [{"name": noun_names[i], "value": noun_values[i]}
                      for i in range(len(noun_names)) if noun_values[i] > 1]
        self.adj = [{"name": adj_names[i], "value": adj_values[i]}
                    for i in range(len(adj_names)) if adj_values[i] > 1]
        self.verbs = [{"name": verb_names[i], "value": verb_values[i]}
                      for i in range(len(verb_names)) if verb_values[i] > 1]
        self.links = [{"name": link_names[i], "value": link_values[i]}
                      for i in range(len(link_names))]
        self.entities = [{"name": entity_names[i], "value": entity_values[i]}
                      for i in range(len(entity_names))]
