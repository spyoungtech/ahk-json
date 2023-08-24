from typing import Any

from .message import JSONResponseMessage

__all__ = ['JSONResponseMessage', 'JSON', 'JXON']


def __getattr__(name: str) -> Any:
    if name == 'JSON':
        from .json import JSON

        return JSON
    elif name == 'JXON':
        from .jxon import JXON

        return JXON
