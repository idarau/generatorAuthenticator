# File that contains Miscelleneous Functions

import numpy as np

def sigmoid(z):
    # sigmoid function
    return 1.0/(1.0+np.exp(-z))

def sigmoidPrime(z):
    # derivative of sigmoid function
    return sigmoid(z)*(1-sigmoid(z))