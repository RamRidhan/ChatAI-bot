

import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork, self).__init__()
        self.a1 = nn.Linear(input_size, hidden_size)
        self.a2 = nn.Linear(hidden_size, hidden_size)
        self.a3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
        
    def ForwardNN(self, z) :
        out = self.a1(z)
        out = self.relu(out)
        out = self.a2(z)
        out = self.relu(out)
        out = self.a3(out)
        return out