
import numpy as np
import json
import random
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from nltk_utilities import bag_of_words, tokenize, stem
from model import NeuralNetwork

with open('intents.json','r') as f:
     intents = json.load(f)
     
aw = []
tags = []
xy = []

for intent in intents['intents'] :
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns'] :
        t = tokenize(pattern)
        aw.extend(t)
        xy.append((t, tag))

ignore_w = ['?', '.', '!']
aw = []
aw = [stem(t) for t in aw if t not in ignore_w]
aw =  sorted(set(aw))
tags = sorted(set(tags))

print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(aw), "unique stemmed words:", aw)


X_train = []
Y_train = []
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, aw)
    X_train.append(bag)
    label = tags.index(tag)
    Y_train.append(label)
    
X_train = np.array(X_train, dtype = object)
Y_train = np.array(Y_train, dtype = object)

# Hyper-parameters 
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)

class ChDat(Dataset):
    def __init__(self):
        self.ns = len(X_train)
        self.xd = X_train
        self.yd = Y_train
        
    def __getitem__(self, i):
        return self.xd[i], self.yd[i]
    
    def __len__(self):
        return self.ns

dataset = ChDat()
train_loader = DataLoader(dataset= dataset, batch_size= batch_size,
                          shuffle = True, num_workers = 0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNetwork(input_size, hidden_size, output_size).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
for epoch in range(num_epochs) :
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        #FORWARD PASS
        outputs = model(words)
        loss = criterion(outputs, labels)
        
        #BACKWARD OPTIMIZE
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
        
print(f'final loss: {loss.item():.4f}')

data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": aw,
"tags": tags
}

FILE = "processor.pth"
torch.save(data, FILE)
print(f'training complete..file saved to {FILE}')
