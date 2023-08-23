from ahk.extensions import Extension

from .util import _get_data_location


class _JSON(Extension):
    def __init__(self):
        super().__init__(includes=[_get_data_location('JSON.ahk')])


JSON = _JSON()
