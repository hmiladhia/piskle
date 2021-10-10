from collections import defaultdict
from functools import partial

from piskle.partial_object import PartialObject, PartialObjectList
from piskle.utils import get_object_class_name


class PisklePartializer:
    def __init__(self):
        self.class_attrs_dict = defaultdict(dict)
        self.custom_partializer_dict = defaultdict(dict)

    def to_partial_obj(self, obj, version=None) -> PartialObject:
        version = self.get_default_version(obj, version) if version is None else version

        # Selecting partializer and obj_attributes
        partialize = self.get_partializer(obj, version)

        if partialize is None:
            return obj

        return partialize(self, obj, version=version)

    def get_partializer(self, obj, version):
        obj_class = type(obj)
        if obj_class in self.custom_partializer_dict:
            partializers = self.custom_partializer_dict[obj_class]
            return partializers.get(None, partializers.get(version, None))

        elif obj_class in self.class_attrs_dict:
            return partial(default_partializer, obj_attributes=self.class_attrs_dict[obj_class][version])
        else:
            return None

    def get_default_params_dict(self, obj, version):
        return None

    def get_default_version(self, obj, version):
        return version

    def register_class_attributes(self, class_, attributes, version):
        self.class_attrs_dict[class_][version] = attributes

    def register_custom_partializer(self, class_, partializer, version=None):
        self.custom_partializer_dict[class_][version] = partializer


def default_partializer(partializer, obj, obj_attributes=None, **meta_dict):
    obj_attributes = [] if obj_attributes is None else obj_attributes

    # Getting the attributes
    model_vars = vars(obj)
    attributes_dict = {attr: partializer.to_partial_obj(model_vars[attr]) for attr in obj_attributes}

    # Creating the partial object
    partial_obj = PartialObject(
        class_name=get_object_class_name(obj),
        attributes=attributes_dict,
    )

    params_dict = partializer.get_default_params_dict(obj, meta_dict.get('version', None))
    if params_dict:
        partial_obj['params'] = params_dict

    if meta_dict:
        partial_obj['meta'] = meta_dict

    return partial_obj


def list_partializer(partializer, obj, **meta_dict):
    type_ = type(obj)
    partial_obj = PartialObjectList(content=type_([partializer.to_partial_obj(o) for o in obj]))

    if meta_dict:
        partial_obj['meta'] = meta_dict

    return partial_obj
