from os.path import dirname as _dir
from os.path import join as _join

from piskle.piskle import Pisklizer
from piskle.sklearn_piskle_partializer import SklearnPisklePartializer
from piskle._piskle_initializer import init_partializer as _init_partializer

sklearn_piskle_partializer = _init_partializer(SklearnPisklePartializer())
sklearn_exporter = Pisklizer(sklearn_piskle_partializer)

with open(_join(_dir(__file__), 'VERSION'), "r", encoding="utf-8") as fh:
    __version__ = fh.read().strip()


def dump(model, file, *args, **kwargs):
    return sklearn_exporter.dump(model, file, *args, **kwargs)


def dumps(model, *args, **kwargs) -> bytes:
    return sklearn_exporter.dumps(model, *args, **kwargs)


def load(file: str) -> object:
    return sklearn_exporter.load(file)


def loads(bytes_object: bytes) -> object:
    return sklearn_exporter.loads(bytes_object)
