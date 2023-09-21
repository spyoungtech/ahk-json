import typing

from ahk.extensions import Extension

from .util import _get_data_location


class _Jxon(Extension):
    def __init__(self):
        super().__init__(includes=[_get_data_location('Jxon.ahk')], requires_autohotkey='v1')


JXON = _Jxon()


@JXON.register
def __jxon_dump(*args, **kwargs) -> typing.NoReturn:
    raise Exception("This isn't supposed to be called")


@JXON.register
async def __jxon_dump(*args, **kwargs) -> typing.NoReturn:
    raise Exception("This isn't supposed to be called")
