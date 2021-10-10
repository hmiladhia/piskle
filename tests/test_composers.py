import warnings

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

import piskle
from utils import compare_size


def information_loss(uploaded_model, model, X_test, y_test):
    score1 = uploaded_model.score(X_test, y_test)
    score2 = model.score(X_test, y_test)
    return score1 == score2


def test_pipeline():
    X, y = datasets.load_iris(return_X_y=True)

    model = Pipeline([('pca', PCA()),
                      ('logistic_regression', LogisticRegression())])

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = model.fit(X, y)

    model_bytes = piskle.dumps(model, optimize=False)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss(piskle_model, model, X, y)

    original_size, piskle_size = compare_size(model, perc=0)
    assert original_size >= piskle_size
