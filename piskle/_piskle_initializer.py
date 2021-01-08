from sklearn.linear_model import LinearRegression, Lasso, Ridge, Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.mixture import GaussianMixture
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor


def init_partializer(sklearn_piskle_partializer):
    sklearn_piskle_partializer.register_class_attributes(LinearRegression, ['coef_', 'intercept_'])
    sklearn_piskle_partializer.register_class_attributes(LogisticRegression, ['classes_', 'coef_', 'intercept_'])
    sklearn_piskle_partializer.register_class_attributes(DecisionTreeClassifier,
                                                         ['n_features_', 'n_outputs_', 'classes_',
                                                          'tree_'])
    sklearn_piskle_partializer.register_class_attributes(Perceptron, ['coef_', 'intercept_', 'classes_'])
    sklearn_piskle_partializer.register_class_attributes(Ridge, ['coef_', 'intercept_'])
    sklearn_piskle_partializer.register_class_attributes(Lasso, ['coef_', 'intercept_'])
    sklearn_piskle_partializer.register_class_attributes(GaussianMixture,
                                                         ['weights_', 'means_', 'precisions_cholesky_'])
    sklearn_piskle_partializer.register_class_attributes(GaussianNB, ['classes_', 'theta_', 'sigma_', 'class_prior_'])
    sklearn_piskle_partializer.register_class_attributes(KNeighborsClassifier,
                                                         ['outputs_2d_', 'classes_', '_y', 'effective_metric_',
                                                          '_fit_method', 'n_samples_fit_', '_tree'])
    sklearn_piskle_partializer.register_class_attributes(KNeighborsRegressor,
                                                         ['_y', 'effective_metric_', '_fit_method', 'n_samples_fit_',
                                                          '_tree'])
    sklearn_piskle_partializer.register_class_attributes(LinearSVC, ['classes_', 'coef_', 'intercept_'])
    sklearn_piskle_partializer.register_class_attributes(DecisionTreeRegressor, ['n_outputs_', 'tree_'])
    sklearn_piskle_partializer.register_class_attributes(MLPClassifier, ['_label_binarizer', 'n_outputs_', 'n_layers_',
                                                                         'out_activation_', 'coefs_', 'intercepts_'])
    sklearn_piskle_partializer.register_class_attributes(MLPRegressor,
                                                         ['n_layers_', 'out_activation_', 'coefs_', 'intercepts_'])
    return sklearn_piskle_partializer


# https://scikit-learn.org/stable/modules/classes.html
"""
sklearn.linear_model.LogisticRegression
sklearn.linear_model.Perceptron
sklearn.linear_model.LinearRegression
sklearn.linear_model.Ridge
sklearn.linear_model.Lasso
mixture.GaussianMixture
naive_bayes.GaussianNB
neighbors.KNeighborsClassifier
neighbors.KNeighborsRegressor
svm.LinearSVC
tree.DecisionTreeRegressor
neural_network.MLPClassifier
neural_network.MLPRegressor

sklearn.feature_extraction.text.CountVectorizer
sklearn.feature_extraction.text.TfidfVectorizer
sklearn.impute.SimpleImputer
preprocessing.LabelEncoder
preprocessing.OneHotEncoder
preprocessing.StandardScaler


sklearn.cluster.KMeans
sklearn.decomposition.FastICA
sklearn.decomposition.PCA
"""
