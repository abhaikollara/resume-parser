import keras_preprocessing
from keras_preprocessing.sequence import pad_sequences
import numpy as np


class Numericalizer:

    def __init__(self):
        self.idx = 0
        self.word2idx = {}

    def numericalize(self, tokens):
        out = []
        for token in tokens:
            try:
                out.append(self.word2idx[token])
            except KeyError:
                self.idx += 1
                self.word2idx[token] = self.idx
                out.append(self.word2idx[token])

        return out

    def __call__(self, tokens):
        return self.numericalize(tokens)


def get_data():
    with open("./data/data.txt") as f:
        # Initial lines are headers
        data = f.readlines()[2:]

    data_X = []
    data_Y = []
    sentence = []
    labels = []
    for line in data:
        items = line.split()
        try:
            word, label = items[0], items[3]
            sentence.append(word)
            labels.append(label)
        except IndexError as e:
            if items == []:
                data_X.append(sentence)
                data_Y.append(labels)
                sentence, labels = [], []
            else:
                print(items)

    word_numer = Numericalizer()
    label_numer = Numericalizer()

    numer_X = [word_numer(seq) for seq in data_X]
    numer_Y = [label_numer(seq) for seq in data_Y]

    X = pad_sequences(numer_X, maxlen=20)
    Y = pad_sequences(numer_Y, maxlen=20)

    return (X, Y)


def main():
    X, Y = get_data()
    np.savez('dataset.npz', [X, Y])

if __name__ == '__main__':
    main()
