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
        common = getattr(self, 'common', None)
        if common:
            return self.data.get('class_name', common.class_name)
        return self.data['class_name']

    @property
    def attributes(self):
        attributes_dict = {}

        common = getattr(self, 'common', None)
        if common:
            attributes_dict.update(common.get('attributes', {}))
        attributes_dict.update(self.data['attributes'])
        return attributes_dict

    @property
    def params(self):
        params_dict = {}
        common = getattr(self, 'common', None)
        if common:
            params_dict.update(common.params)
        params_dict.update(self.data.get('params', {}))
        return params_dict

    @property
    def fullobject(self) -> object:
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


class PartialObjectList(PartialObjectBase):
    @property
    def content(self):
        return self.data['content']

    @property
    def type(self):
        return type(self.content)

    @property
    def common(self):
        return self.data.get('common', None)

    @property
    def fullobject(self) -> object:
        object_list = []
        for obj in self.content:
            if self.common:
                obj.common = self.common
            object_list.append(obj.fullobject if isinstance(obj, PartialObjectBase) else obj)
        return self.type(object_list)
