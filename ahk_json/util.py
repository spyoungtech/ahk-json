import os
import pathlib

_root = pathlib.Path(__file__).parent


def _get_data_location(name: str) -> str:
    location = _root.joinpath(name)
    assert os.path.exists(location)
    return str(location.absolute())
