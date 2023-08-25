# ahk-json

This is an extension package intended to be used with the Python [ahk](https://github.com/spyoungtech/ahk) package.

It provides interfaces from [cocobelgica/AutoHotkey-JSON](https://github.com/cocobelgica/AutoHotkey-JSON) for
working with JSON in AutoHotkey. The extensions in this package do not provide any additional methods,
but simply provide a convenient way to include `Jxon.ahk` and/or `JSON.ahk` into other extensions.

This package provides two extensions: `JXON` and `JSON`. It also registers a JSON message type (`ahk_json.message.JsonResponseMessage`)

## Installation

Install this extension using `pip`

```python
pip install ahk-json
```

# Usage

Typically, you use this as a dependency when building your own extensions.

In the following example, a simple extension (`my_extension`) is created. It implements an AHK function `MyTestFunction`
-- the registered to the extension using the Python function `my_test_function`.
```python
from ahk.extensions import Extension
from ahk import AHK

from ahk_json import JXON  # importing is necessary for ``extensions='auto'`` to work, even if this is not used

ext_script = '''\
MyTestFunction(ByRef command) {
    arg := command[2]
    obj := Object("test", arg)
    res := Jxon_Dump(obj) ; this is available thanks to the extension
    return FormatResponse("ahk_json.message.JsonResponseMessage", res)
}
'''

my_extension = Extension(script_text=ext_script)

@my_extension.register
def my_test_function(ahk: AHK, arg: str):
    return ahk.function_call('MyTestFunction', [arg])


def main():
    ahk = AHK(extensions='auto')  # automatically use all imported/created extensions
    # or use the extensions explicitly:
    # ahk = AHK(extensions=[JXON, my_extension])

    # now ``.my_test_function`` is a method on the `ahk` instance:
    assert ahk.my_test_function('foo') == {'test': 'foo'}
```


# License

This work is licensed under the MIT license.

This package includes substantial portions of the [original AutoHotkey-JSON](https://github.com/cocobelgica/AutoHotkey-JSON).
The code included from AutoHotkey-JSON is owned and copyrighted by its original author(s) and is used/redistributed
under the terms of the [WTFPL](http://www.wtfpl.net).
