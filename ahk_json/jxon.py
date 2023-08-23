from ahk.extensions import Extension

from .util import _get_data_location


class _Jxon(Extension):
    def __init__(self):
        super().__init__(includes=[_get_data_location('Jxon.ahk')])


JXON = _Jxon()
