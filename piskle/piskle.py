import pickle
import pickletools

from piskle.partializer import PartialObject
from piskle.partializer import PisklePartializer


class Pisklizer:
    # TODO: extend to use joblib and include compression
    # TODO: move serializer as dumps option
    def __init__(self, partializer=None, serializer='pickle'):
        self.partializer = partializer or PisklePartializer()
        self.serializer = serializer

    def dumps(self, obj: object, *args, **kwargs) -> bytes:
        new_obj = self.partializer.to_partial_obj(obj)

        return self._dumps(new_obj, *args, **kwargs)

    def dump(self, obj: object, file: str, *args, **kwargs):
        new_obj = self.partializer.to_partial_obj(obj)

        self._dump(new_obj, file, *args, **kwargs)

    def loads(self, bytes_object: bytes) -> object:
        exported_model = self._loads(bytes_object)

        if isinstance(exported_model, PartialObject):
            model = self.partializer.from_partial_obj(exported_model)
        else:
            model = exported_model

        return model

    def load(self, file: str) -> object:
        exported_model = self._load(file)

        if isinstance(exported_model, PartialObject):
            model = self.partializer.from_partial_obj(exported_model)
        else:
            model = exported_model

        return model

    # Utility functions
    def _dumps(self, obj: object, optimize=True) -> bytes:
        assert self.serializer == 'pickle'

        bytes_object = pickle.dumps(obj)
        if optimize:
            return pickletools.optimize(bytes_object)
        return bytes_object

    def _dump(self, obj: object, file_path: str, optimize=True):
        with open(file_path, 'wb') as f:
            bytes_object = self._dumps(obj, optimize=optimize)
            f.write(bytes_object)

    def _loads(self, bytes_object: bytes) -> object:
        assert self.serializer == 'pickle'
        return pickle.loads(bytes_object)

    def _load(self, file: str) -> object:
        assert self.serializer == 'pickle'
        with open(file, 'rb') as f:
            obj = pickle.load(f)
        return obj
