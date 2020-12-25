from sklearn_exporter.exporter import SklearnExporter


sklearn_exporter = SklearnExporter()


def dump(model, file):
    return sklearn_exporter.dump(model, file)


def load(file):
    return sklearn_exporter.load(file)
