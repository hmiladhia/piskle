from piskle.piskle import Pisklizer
from piskle.sklearn_piskle_partializer import SklearnPisklePartializer

sklearn_piskle_partializer = SklearnPisklePartializer()
sklearn_exporter = Pisklizer(sklearn_piskle_partializer)


def dump(model, file, *args, **kwargs):
    return sklearn_exporter.dump(model, file, *args, **kwargs)


def load(file):
    return sklearn_exporter.load(file)


from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier


sklearn_piskle_partializer.register_class_attributes(LinearRegression, ['coef_', 'intercept_'])
sklearn_piskle_partializer.register_class_attributes(DecisionTreeClassifier, ['n_features_', 'n_outputs_', 'classes_',
                                                                              'tree_'])
sklearn_piskle_partializer.register_class_attributes(MLPClassifier, ['n_features_in_', '_label_binarizer', 'classes_',
                                                                     'n_outputs_', 'n_layers_', 'out_activation_',
                                                                     'coefs_', 'intercepts_'])
