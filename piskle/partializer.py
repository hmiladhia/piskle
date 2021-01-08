from collections import defaultdict
from functools import partial

from piskle.utils import get_object_class_name, import_object


class PartialObject(dict):
    pass


class PisklePartializer:
    def __init__(self):
        self.class_attrs_dict = defaultdict(dict)
        self.custom_partializer_dict = defaultdict(dict)

    def from_partial_obj(self, partial_obj: PartialObject):
        # TODO: warning on sklearn version metadata mismatch
        # Getting the estimator class
        obj_class = import_object(*partial_obj['class_name'])

        # Instantiating the estimator
        model = obj_class(**partial_obj['params'])

        # Assigning the attributes to the estimator
        for attribute_name, attribute_value in partial_obj['attributes'].items():
            setattr(model, attribute_name, attribute_value)

        return model

    def to_partial_obj(self, obj, params_dict=None, version=None) -> PartialObject:
        version = self.get_default_version(obj, version) if version is None else version

        # Selecting partializer and obj_attributes
        partialize = self.get_partializer(obj, version)

        if partialize is None:
            return obj

        params_dict = self.get_default_params_dict(obj, version, params_dict)

        return partialize(obj, params_dict, version)

    def get_partializer(self, obj, version):
        obj_class = type(obj)
        if obj_class in self.custom_partializer_dict:
            return self.custom_partializer_dict[obj_class][version]
        elif obj_class in self.class_attrs_dict:
            return partial(self.default_partializer, obj_attributes=self.class_attrs_dict[obj_class][version])
        return None

    def get_default_params_dict(self, obj, version, params_dict):
        return params_dict

    def get_default_version(self, obj, version):
        return version

    def default_partializer(self, obj, params_dict=None, version=None, obj_attributes=None):
        obj_attributes = [] if obj_attributes is None else obj_attributes

        # TODO: include module version: in meta or in version ?

        # Getting the attributes
        model_vars = vars(obj)
        attributes_dict = {attr: model_vars[attr] for attr in obj_attributes}

        # Creating the partial object
        partial_obj = PartialObject(
            class_name=get_object_class_name(obj),
            attributes=attributes_dict,
            params=params_dict
        )
        return partial_obj

    def register_class_attributes(self, class_, attributes, version):
        self.class_attrs_dict[class_][version] = attributes
