import numpy as np
from scipy.stats import mode

def msn(data):
    """
    Calcula a média de uma lista ou array.
    """
    return np.mean(data)

def mdn(data):
    """
    Calcula a mediana de uma lista ou array.
    """
    return np.median(data)

def modc(data):
    """
    Calcula a moda de uma lista ou array.
    """
    moda_resultado = mode(data, keepdims=True)
    return moda_resultado.mode[0]