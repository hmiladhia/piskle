import warnings

import pytest
from sklearn import datasets
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier

import piskle
from utils import compare_size


def information_loss(uploaded_model, model, X_test, y_test):
    score1 = uploaded_model.score(X_test, y_test)
    score2 = model.score(X_test, y_test)
    return score1 == score2


@pytest.mark.parametrize('model_class', [
    LogisticRegression,
    Perceptron,
    GaussianNB,
    KNeighborsClassifier,
    MLPClassifier,
    LinearSVC,
    DecisionTreeClassifier,
])
def test_classification_models(model_class):
    X, y = datasets.load_iris(return_X_y=True)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = model_class().fit(X, y)

    model_bytes = piskle.dumps(model, optimize=False)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss(piskle_model, model, X, y)

    original_size, piskle_size = compare_size(model, model_bytes, perc=10)
    assert original_size >= piskle_size


