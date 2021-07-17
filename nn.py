import numpy as np


class NeuralNetwork:

    def __init__(self, layer_sizes):
        # layer_sizes example: [4, 10, 2]  -> input, hidden, output
        self.layer_sizes = layer_sizes
        self.weights = dict()
        self.biases = dict()
        for layer_number in range(1, self.network_size):
            self.weights[layer_number] = np.random.normal(
                size=(self.layer_sizes[layer_number], self.layer_sizes[layer_number - 1]))
            self.biases[layer_number] = np.zeros(shape=(self.layer_sizes[layer_number], 1))
        # print(self.biases[2].shape)

    @property
    def network_size(self):
        return len(self.layer_sizes)

    @staticmethod
    def activation(array):
        return 1 / (1 + np.exp(-array))

    def forward(self, _input: np.array):
        layers = {
            0: _input
        }
        for layer_number in range(1, self.network_size):
            layers[layer_number] = self.activation(
                np.matmul(self.weights[layer_number], layers[layer_number - 1]) + self.biases[layer_number])
        return layers[self.network_size - 1].copy()

    def copy(self):
        new_nn = NeuralNetwork(self.layer_sizes)
        new_nn.weights = self.weights.copy()
        new_nn.biases = self.biases.copy()
        return new_nn
