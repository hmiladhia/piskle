from abc import ABC, abstractmethod
from collections import UserDict
from piskle.utils import import_object


class PartialObjectBase(UserDict, ABC):
    @property
    def meta(self):
        return self.data.get('meta', {})

    @property
    @abstractmethod
    def fullobject(self):
        raise NotImplementedError


class PartialObject(PartialObjectBase):
    @property
    def class_name(self):
        return self.data['class_name']

    @property
    def attributes(self):
        return self.data['attributes']

    @property
    def params(self):
        return self.data.get('params', {})

    @property
    def fullobject(self):
        # Getting object class
        obj_class = import_object(*self.class_name)

        # Instantiating the object
        model = object.__new__(obj_class)

        if self.params:
            model.__init__(**self.params)

        # Assigning object attributes
        for attribute_name, attribute_value in self.attributes.items():
            if isinstance(attribute_value, PartialObjectBase):
                attribute_value = attribute_value.fullobject
            setattr(model, attribute_name, attribute_value)

        return model
