from ahk import AHK
from ahk.extensions import Extension

from ahk_json import JXON

ext_script = '''\
MyTestFunction(ByRef command) {
    arg := command[2]
    obj := Object("test", arg)
    res := Jxon_Dump(obj)
    return FormatResponse("ahk_json.message.JsonResponseMessage", res)
}
'''

my_extention = Extension(script_text=ext_script)


@my_extention.register
def myfunc(self, arg: str) -> dict[str, str]:
    return self._transport.function_call('MyTestFunction', args=[arg])


def test_jxon():
    ahk = AHK(extensions=[JXON, my_extention])
    assert ahk.myfunc('hello') == {'test': 'hello'}


def test_jxon_auto():
    ahk = AHK(extensions='auto')
    assert ahk.myfunc('hello') == {'test': 'hello'}
