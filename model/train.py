import numpy as np
import torch
import pytorch_pretrained_bert
from pytorch_pretrained_bert import BertForTokenClassification
from pytorch_pretrained_bert import BertConfig
from data import get_data

VOCAB_SIZE = 10000

X, Y = get_data()

xt = torch.from_numpy(X).long()
yt = torch.from_numpy(Y).long()

x_train, y_train = [x[700:] for x in [xt, yt]]
x_test, y_test = [x[:700] for x in [xt, yt]]

model = BertForTokenClassification(BertConfig(VOCAB_SIZE), 10)
params = [x for x in model.parameters()][-2]
optimizer = torch.optim.Adam([params])
criterion = torch.nn.NLLLoss()


for i in range(0, len(x_train), 16):
    # break
    batch_x = x_train[i:i+16]
    batch_y = y_train[i:i+16]
    batch_y = batch_y.unsqueeze(-1)
    optimizer.zero_grad()

    loss = model(batch_x, labels=batch_y)
    loss.backward()

    optimizer.step()
    print(loss.item())
