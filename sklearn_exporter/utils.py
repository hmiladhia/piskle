import importlib


def import_object(name, class_name):
    return getattr(importlib.import_module(name), class_name)


def get_object_class_name(o):
    cls = o.__class__
    module_name, class_name = cls.__module__, cls.__name__
    return module_name,  class_name
