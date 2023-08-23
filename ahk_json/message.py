import json
from typing import Any

from ahk.message import ResponseMessage


class JSONResponseMessage(ResponseMessage):
    type = 'json'

    def unpack(self) -> Any:
        return json.loads(self._raw_content)
