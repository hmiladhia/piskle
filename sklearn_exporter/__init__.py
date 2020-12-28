from sklearn_exporter.piskle import Pisklizer


sklearn_exporter = Pisklizer()


def dump(model, file):
    return sklearn_exporter.dump(model, file)


def load(file):
    return sklearn_exporter.load(file)
