import numpy as np
import random
import pygame
from otherFunctions import sigmoid, sigmoidPrime

# Miscellaneous Functions
class generatorNetwork():
    def __init__(self, sizes, copyNetwork=None, var=0.02):
        # If inheriting weights and biases from another generation
        if copyNetwork is None:
            #Saving Attributes
            self.numLayers = len(sizes)
            self.sizes = sizes
            self.weights = []
            self.biases = []

            # Initializing all weights and biases in a list - weights are a list of list
            for layerNumber in range (1, self.numLayers):
                self.biases.append(np.random.randn(self.sizes[layerNumber], 1))
                self.weights.append(np.random.randn(self.sizes[layerNumber - 1],
                                                    self.sizes[layerNumber]))

        # Copying over elements
        else:
            self.weights = copyNetwork.weights
            self.biases = copyNetwork.biases

        # Mutating the weights and biases
        for layerNumber in range (1, self.numLayers):
            self.biases.




    def feedForward(self, a):
        # return output from list of outputs from list of inputs (each go into a neuron)
        for b, w in zip(self.biases, self.weights):
            z = sigmoid(np.dot(w, a)+b)
        return z


