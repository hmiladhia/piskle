import pickle
import piskle


def compare_size(model, perc=20):
    pickle_size = len(pickle.dumps(model)) * (100+perc)/100
    piskle_size = len(piskle.dumps(model, optimize=False))
    return pickle_size, piskle_size
