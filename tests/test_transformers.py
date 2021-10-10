import warnings
import random

import pytest
from sklearn import datasets
from sklearn.decomposition import FastICA, PCA
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.impute import SimpleImputer

import piskle


def load_texts(n=1000):
    lorem = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure delectus, nisi laudantium a sint pariatur " \
            "officiis minus, laboriosam eius possimus repellat error ut itaque, blanditiis doloremque veritatis neque " \
            "tempora eum. "
    return [lorem[:random.randint(1, len(lorem))] for _ in range(n)]


def information_loss(model1, model2, X_test):
    y_transformed1 = model1.transform(X_test)
    y_transformed2 = model2.transform(X_test)

    return (y_transformed1 == y_transformed2).all()


def information_loss_sparse(model1, model2, X_test):
    y_transformed1 = model1.transform(X_test)
    y_transformed2 = model2.transform(X_test)

    return not (y_transformed1 != y_transformed2).toarray().any()


@pytest.mark.parametrize('model_class', [
    FastICA,
    PCA,
    SimpleImputer
])
def test_numerical_transformers_models(model_class):
    X, _ = datasets.load_iris(return_X_y=True)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = model_class().fit(X)

    model_bytes = piskle.dumps(model)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss(piskle_model, model, X)


@pytest.mark.parametrize('model_class', [
    CountVectorizer,
    TfidfVectorizer,
])
def test_text_transformers_models(model_class):
    X = load_texts()

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = model_class().fit(X)

    model_bytes = piskle.dumps(model)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss_sparse(piskle_model, model, X)
