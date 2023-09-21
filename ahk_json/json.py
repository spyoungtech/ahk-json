from typing import NoReturn

from ahk.extensions import Extension

from .util import _get_data_location


class _JSON(Extension):
    def __init__(self):
        super().__init__(includes=[_get_data_location('JSON.ahk')], requires_autohotkey='v1')


JSON = _JSON()


@JSON.register
def __json_dump(*args, **kwargs) -> NoReturn:
    raise Exception("This isn't supposed to be called")


@JSON.register
async def __json_dump(*args, **kwargs) -> NoReturn:
    raise Exception("This isn't supposed to be called")
