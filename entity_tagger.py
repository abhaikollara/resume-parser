from collections import namedtuple
import spacy
nlp = spacy.load('en')

Tag = namedtuple('EntityTag', ['entity', 'label'])


def spacy_tagger(text):
    parsed = nlp(text)
    tags = []
    for ent in parsed.ents:
        tags.append(Tag(str(ent).strip(), ent.label_))

    return tags


def custom_tagger(text):
    # Should return a list of Tags
    raise NotImplementedError
