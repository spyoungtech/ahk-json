from typing import Any

from .message import JSONResponseMessage

__all__ = ['JSONResponseMessage', 'JSON', 'Jxon']


def __getattr__(name: str) -> Any:
    if name == 'JSON':
        from .json import JSON

        return JSON
    elif name == 'Jxon':
        from .jxon import Jxon

        return Jxon
