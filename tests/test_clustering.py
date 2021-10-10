import warnings

import pytest
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

import piskle
from utils import compare_size


def information_loss(model1, model2, X_test):
    y_pred1 = model1.predict(X_test)
    y_pred2 = model2.predict(X_test)
    return (y_pred1 == y_pred2).all()


@pytest.mark.parametrize('model_class', [
    KMeans,
    GaussianMixture,
])
def test_unsupervised_models(model_class):
    X, _ = datasets.load_iris(return_X_y=True)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = model_class().fit(X)

    model_bytes = piskle.dumps(model, optimize=False)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss(piskle_model, model, X)

    original_size, piskle_size = compare_size(model, perc=5)
    assert original_size >= piskle_size
