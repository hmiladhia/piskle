import random
import pickle
import piskle


def compare_size(model, perc=20):
    pickle_size = len(pickle.dumps(model)) * (100+perc)/100
    piskle_size = len(piskle.dumps(model, optimize=False))
    return pickle_size, piskle_size


def load_texts(n=1000):
    lorem = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure delectus, nisi laudantium a sint pariatur " \
            "officiis minus, laboriosam eius possimus repellat error ut itaque, blanditiis doloremque veritatis neque " \
            "tempora eum. "
    return [lorem[:random.randint(1, len(lorem))] for _ in range(n)]
