from sklearn_exporter.utils import get_object_class_name, import_object


class PartialObject(dict):
    pass


class PisklePartializer:
    def default_partializer(self, obj, params_dict=None, version=None,  model_attributes=None):
        model_attributes = [] if model_attributes is None else model_attributes

        # TODO: include module version

        # Getting the attributes
        model_vars = vars(obj)
        attributes_dict = {attr: model_vars[attr] for attr in model_attributes}

        # Creating the partial object
        partial_obj = PartialObject(
            class_name=get_object_class_name(obj),
            attributes=attributes_dict,
            params=params_dict
        )
        return partial_obj

    def to_partial_obj(self, obj, params_dict=None, version=None, ):
        # Selecting partializer and model_attributes
        model_attributes = self.__get_model_attributes(obj.__class__)
        partialize = self.default_partializer

        return obj if model_attributes is None else partialize(obj, params_dict, version, model_attributes)

    def from_partial_obj(self, partial_obj):
        # TODO: warning on sklearn version metadata mismatch
        # Getting the estimator class
        obj_class = import_object(*partial_obj['class_name'])

        # Instantiating the estimator
        model = obj_class(**partial_obj['params'])

        # Assigning the attributes to the estimator
        for attribute_name, attribute_value in partial_obj['attributes'].items():
            setattr(model, attribute_name, attribute_value)

        return model
