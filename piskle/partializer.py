from collections import defaultdict
from functools import partial

from piskle.partial_object import PartialObjectBase, PartialObject, PartialObjectList
from piskle.utils import get_object_class_name


MISSING = object()


class PisklePartializer:
    def __init__(self):
        self.class_attrs_dict = defaultdict(dict)
        self.custom_partializer_dict = defaultdict(dict)

    def to_partial_obj(self, obj, version=None) -> PartialObjectBase:
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
    attributes_dict = {attr: partializer.to_partial_obj(getattr(obj, attr))
                       for attr in obj_attributes if getattr(obj, attr, MISSING) is not MISSING}

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
    same_type_list = len(obj) > 1 and len({type(o) for o in obj}) == 1

    type_ = type(obj)
    partial_obj = PartialObjectList(content=type_([partializer.to_partial_obj(o) for o in obj]))

    if same_type_list and all(isinstance(o, PartialObject) for o in partial_obj.content):
        common = factorize_partial_obj(partial_obj.content)
        for o in partial_obj['content']:
            o.common = common

    if meta_dict:
        partial_obj['meta'] = meta_dict

    return partial_obj


def factorize_partial_obj(partial_obj_list):
    common = PartialObject()
    if len({obj.class_name for obj in partial_obj_list}) == 1:
        common['class_name'] = partial_obj_list[0].class_name
        for obj in partial_obj_list:
            obj.pop('class_name', None)

    if partial_obj_list[0].params:
        common_params = factorize_dict([obj['params'] for obj in partial_obj_list])
        if common_params:
            common['params'] = common_params

    if partial_obj_list[0].attributes:
        common_attributes = factorize_dict([obj['attributes'] for obj in partial_obj_list])
        if common_attributes:
            common['attributes'] = common_attributes

    return common


def factorize_dict(dicts: list):
    sample_dict = dicts[0]
    keys = set(sample_dict)
    for d in dicts[1:]:
        keys &= set(d)

    if not keys:
        return

    common = {}
    for key in keys:
        value = sample_dict[key]
        if all(d[key] is value for d in dicts[1:]):
            for d in dicts:
                d.pop(key, None)
            common[key] = value

    return common
