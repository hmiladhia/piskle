import pickle
import pickletools

from sklearn_exporter.utils import get_object_class_name, import_object


class SklearnExportedObject(dict):
    pass

# TODO: Implement GET keys depending on version class


class SklearnExporter:
    # TODO: Turn into a base class PartialExporter
    # TODO: Implement dumps
    def dump(self, model, file, *args, **kwargs):
        model_attributes = self.get_model_attributes(model)

        serialized_obj = self.get_serialized_obj(model, model_attributes)

        self._dump(serialized_obj, file, *args, **kwargs)

    def load(self, file):
        with open(file, 'rb') as f:
            exported_model = pickle.load(f)
        # TODO: warning on sklearn version mismatch
        if isinstance(exported_model, SklearnExportedObject):
            estimator_class = import_object(*exported_model['estimator'])
            model = estimator_class(**exported_model['params'])
            for attribute_name, attribute_value in exported_model['attributes'].items():
                setattr(model, attribute_name, attribute_value)
        else:
            model = exported_model
        return model

    def get_model_attributes(self, model):
        # TODO: MAYBE PUT this in another class
        # TODO: USE REGISTER PATTERN
        model_params = None
        model_class = model.__class__.__name__
        if model_class == 'LinearRegression':
            model_params = ['coef_', 'intercept_']  # '_residues', 'singular_', 'rank_', 'n_features_in_',
        elif model_class == 'MLPClassifier':
            model_params = ['n_features_in_', '_label_binarizer', 'classes_', 'n_outputs_',
                            'n_layers_', 'out_activation_', 'coefs_', 'intercepts_']

        return model_params

    def get_serialized_obj(self, model, model_params):
        if model_params is None:
            serialized_obj = model
        else:
            # TODO: include sklearn version
            model_vars = vars(model)
            attributes_dict = {param: model_vars[param] for param in model_params}
            params_dict = model.get_params()
            serialized_obj = SklearnExportedObject(
                estimator=get_object_class_name(model),
                attributes=attributes_dict,
                params=params_dict
            )
        return serialized_obj

    @staticmethod
    def _dump(obj, file_path, optimize=True):
        with open(file_path, 'wb') as f:
            if optimize:
                obj = pickletools.optimize(pickle.dumps(obj))
                f.write(obj)
            else:
                pickle.dump(obj, f)

