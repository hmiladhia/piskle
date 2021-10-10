from sklearn.cluster import KMeans
from sklearn.decomposition import FastICA, PCA
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression, Lasso, Ridge, Perceptron
from sklearn.mixture import GaussianMixture
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.pipeline import Pipeline

from piskle.partializer import list_partializer


def init_partializer(sklearn_piskle_partializer):
    sklearn_piskle_partializer.register_custom_partializer(list, list_partializer)
    sklearn_piskle_partializer.register_custom_partializer(set, list_partializer)
    sklearn_piskle_partializer.register_custom_partializer(tuple, list_partializer)

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
    sklearn_piskle_partializer.register_class_attributes(SimpleImputer, ['statistics_'])
    sklearn_piskle_partializer.register_class_attributes(StandardScaler, ['mean_', 'scale_'])
    sklearn_piskle_partializer.register_class_attributes(FastICA, ['components_', 'mean_'])
    sklearn_piskle_partializer.register_class_attributes(PCA, ['mean_', 'components_'])
    sklearn_piskle_partializer.register_class_attributes(KMeans, ['_n_threads', 'cluster_centers_'])
    sklearn_piskle_partializer.register_class_attributes(CountVectorizer, ['vocabulary_'])
    sklearn_piskle_partializer.register_class_attributes(TfidfVectorizer, ['_tfidf', 'vocabulary_'])

    sklearn_piskle_partializer.register_class_attributes(LabelEncoder, ['classes_'])
    sklearn_piskle_partializer.register_class_attributes(OneHotEncoder, ['categories_', 'drop_idx_'])
    sklearn_piskle_partializer.register_class_attributes(Pipeline, ['steps'])
    return sklearn_piskle_partializer


# List of all modules:
# https://scikit-learn.org/stable/modules/classes.html
