from collections import namedtuple

Tag = namedtuple('EntityTag', ['entity', 'label'])

class SpacyTagger:

    def __init__(self):
        import spacy
        self.nlp = spacy.load('en')

    def tag(self, text):
        parsed = self.nlp(text)
        tags = []
        for ent in parsed.ents:
            tags.append(Tag(str(ent).strip(), ent.label_))

        return tags

    def __call__(self, text):
        return self.tag(text)


class BERTTagger:

    def __init__(self):
        print("Initializng Tagger")
        print("This might take a while")
        from model.bert import Ner
        self.model = Ner("./model/saved_model/")

    def tag(self, text):
        prediction = self.model.predict(text)
        tags = []
        current_tag = []
        for ent, pred in prediction.items():
            tag = pred['tag']
            if tag == 'O':
                continue
            elif tag[0] == 'B':
                tags.append(current_tag)
                current_tag = [ent, tag[2:]]
            elif tag[0] == 'I':
                current_tag[0] += " " + ent

        tags.append(current_tag)

        tags = [Tag(x[0], x[1]) for x in tags[1:]]

        return tags

    def __call__(self, text):
        return self.tag(text)
