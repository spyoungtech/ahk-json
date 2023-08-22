import os
import pathlib

from ahk.extensions import Extension

_root = pathlib.Path(__file__).parent


def _get_data_location(name: str) -> str:
    location = _root.joinpath(name)
    assert os.path.exists(location)
    return str(location.absolute())


class JSON(Extension):
    def __init__(self):
        super().__init__(includes=[_get_data_location('JSON.ahk')])


class Jxon(Extension):
    def __init__(self):
        super().__init__(includes=[_get_data_location('Jxon.ahk')])
