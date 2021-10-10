import random
import warnings

import pytest
import numpy as np
from sklearn import datasets
from sklearn.decomposition import FastICA, PCA
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer

import piskle
from utils import compare_size
from utils import load_texts


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
    SimpleImputer,
    StandardScaler,
])
def test_numerical_transformers_models(model_class):
    X, _ = datasets.load_iris(return_X_y=True)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = model_class().fit(X)

    model_bytes = piskle.dumps(model, optimize=False)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss(piskle_model, model, X)

    original_size, piskle_size = compare_size(model)
    assert original_size >= piskle_size


def test_label_encoder_models():
    X = np.array([f'class_{random.randint(0, 9)}' for _ in range(1000)])

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = LabelEncoder().fit(X)

    model_bytes = piskle.dumps(model, optimize=False)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss(piskle_model, model, X)

    original_size, piskle_size = compare_size(model)
    assert original_size >= piskle_size


def test_one_hot_encoder_models():
    X = np.array([[f'class_{random.randint(0, 5)}' for _ in range(1000)]])

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = OneHotEncoder().fit(X)

    model_bytes = piskle.dumps(model, optimize=False)
    piskle_model = piskle.loads(model_bytes)

    assert information_loss_sparse(piskle_model, model, X)

    original_size, piskle_size = compare_size(model)
    assert original_size >= piskle_size


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

    original_size, piskle_size = compare_size(model, perc=5)
    assert original_size >= piskle_size
