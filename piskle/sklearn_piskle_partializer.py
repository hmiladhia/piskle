from sklearn import __version__ as sklearn_version
from sklearn.pipeline import Pipeline

from piskle.piskle import PisklePartializer


class SklearnPisklePartializer(PisklePartializer):
    def get_default_params_dict(self, obj, version):
        if isinstance(obj, Pipeline):
            return super().get_default_params_dict(obj, version)
        return obj.get_params()

    def register_class_attributes(self, class_, attributes, version=None):
        version = sklearn_version if version is None else version
        return super().register_class_attributes(class_, attributes, version)

    def get_default_version(self, obj, version):
        return sklearn_version
