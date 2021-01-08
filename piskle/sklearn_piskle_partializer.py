from sklearn import __version__ as sklearn_version

from piskle.piskle import PisklePartializer


class SklearnPisklePartializer(PisklePartializer):
    def get_default_params_dict(self, obj, version, params_dict):
        return obj.get_params() if params_dict is None else params_dict

    def register_class_attributes(self, class_, attributes, version=None):
        version = sklearn_version if version is None else version
        return super().register_class_attributes(class_, attributes, version)

    def get_default_version(self, obj, version):
        return sklearn_version
