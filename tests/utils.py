import pickle


def compare_size(model, binary_model, perc=20):
    piskle_size = len(binary_model)
    size = len(pickle.dumps(model)) * (100+perc)/100
    return size, piskle_size
