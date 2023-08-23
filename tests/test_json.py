from ahk import AHK
from ahk.extensions import Extension

from ahk_json import JSON
from ahk_json import Jxon

ext_script = '''\
MyTestFunction(ByRef command) {
    global JSONRESPONSEMESSAGE
    arg := command[2]
    obj := Object("test", arg)
    res := Jxon_Dump(obj)
    return FormatResponse(JSONRESPONSEMESSAGE, res)
}
'''

my_extention = Extension(script_text=ext_script)


@my_extention.register
def myfunc(self, arg: str) -> dict[str, str]:
    return self._transport.function_call('MyTestFunction', args=[arg])


def test_jxon():
    ahk = AHK(extensions=[Jxon(), my_extention])
    assert ahk.myfunc('hello') == {'test': 'hello'}
