# Piskle

![pyversions](https://img.shields.io/pypi/pyversions/piskle) ![wheel](https://img.shields.io/pypi/wheel/piskle) ![license](https://img.shields.io/pypi/l/piskle) ![version](https://img.shields.io/pypi/v/piskle)

`Piskle` allows you to selectively serialize python objects to save on memory and load times. 

It has special support for exporting `scikit-learn`'s  models in an optimized way, 
exporting exactly what's needed to make predictions.

![Banner](https://media.giphy.com/media/QVhHtKMbPZAzoKLUG2/giphy.gif)
<p><a href="https://giphy.com/gifs/rickandmorty-season-3-adult-swim-rick-and-morty-QVhHtKMbPZAzoKLUG2">via GIPHY</a></p>

## Example:
To use `piskle`, you first need a model to export. You can use this as an example:

```python
from sklearn import datasets
from sklearn.neural_network import MLPClassifier

data = datasets.load_iris()

model = MLPClassifier().fit(data.data, data.target)
```

Exporting the model is then as easy as the following:
```python
import piskle

piskle.dump(model, 'model.pskl')
```

Loading it is even easier:
```python
model = piskle.load('model.pskl')
```

If you want even faster serialization, you can disable the `optimize` feature. 
Note that this feature reduces the size of the exported file even further and improves loading time.
```python
piskle.dump(model, 'model.pskl', optimize=False)
```

## Currently Supported Models
### Predictors ( Classifiers, Regressors, ...)
|       Estimator        |       Reference        |
| :--------------------: | :--------------------: |
|       LinearSVC        |      sklearn.svm       |
|    LinearRegression    |  sklearn.linear_model  |
|   LogisticRegression   |  sklearn.linear_model  |
|         Lasso          |  sklearn.linear_model  |
|         Ridge          |  sklearn.linear_model  |
|       Perceptron       |  sklearn.linear_model  |
|       GaussianNB       |  sklearn.naive_bayes   |
|  KNeighborsRegressor   |   sklearn.neighbors    |
|  KNeighborsClassifier  |   sklearn.neighbors    |
|     MLPClassifier      | sklearn.neural_network |
|      MLPRegressor      | sklearn.neural_network |
| DecisionTreeClassifier |      sklearn.tree      |
| DecisionTreeRegressor  |      sklearn.tree      |
|         KMeans         |    sklearn.cluster     |
|    GaussianMixture     |    sklearn.mixture     |
### Transformers
|    Estimator    |            Reference            |
| :-------------: | :-----------------------------: |
|       PCA       |      sklearn.decomposition      |
|     FastICA     |      sklearn.decomposition      |
| CountVectorizer | sklearn.feature_extraction.text |
| TfidfVectorizer | sklearn.feature_extraction.text |
|  SimpleImputer  |         sklearn.impute          |
| StandardScaler  |      sklearn.preprocessing      |
|  LabelEncoder   |      sklearn.preprocessing      |
|  OneHotEncoder  |      sklearn.preprocessing      |

## Future Improvements
This is still an early working version of piskle, there are still a few improvements planned:
- More thorough testing
- Version Management: Support for more versions of scikit-learn (earlier versions)
- Support for more Estimators (Feel free to contact us for a specific request)
- Support for "Nested" Estimators (Pipelines, RandomForests, etc...)
- Support for other serialization methods (such as joblib, shelve or json...)

## Contribute
As this is still a work in progress, while using piskle, you might encounter some bugs.
It would be a great help to us, if you could **report them in the github repo**.

Feel free, to share with us any potential improvements you'd like to see in piskle.



If you like the project and want to support us, you can buy us a coffee here:

<a href="https://www.buymeacoffee.com/amal.hasni" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>




