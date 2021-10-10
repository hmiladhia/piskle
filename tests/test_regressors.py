import warnings

import pytest
from sklearn import datasets
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor

import piskle
from utils import compare_size


def information_loss(uploaded_model, model, X_test, y_test):
    score1 = uploaded_model.score(X_test, y_test)
    score2 = model.score(X_test, y_test)
    return score1 == score2


@pytest.mark.parametrize('model_class', [
    LinearRegression,
    DecisionTreeRegressor,
    MLPRegressor,
    KNeighborsRegressor,
    Lasso,
    Ridge,
])
def test_regression_models(model_class):
    X, y = datasets.load_diabetes(return_X_y=True)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = model_class().fit(X, y)

    model_bytes = piskle.dumps(model, optimize=False)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss(piskle_model, model, X, y)

    original_size, piskle_size = compare_size(model, model_bytes)
    assert original_size >= piskle_size



