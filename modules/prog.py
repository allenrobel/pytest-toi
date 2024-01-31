#!/usr/bin/env python
from modules.baz import Baz

baz = Baz()
baz.do_something()
print(f"foo_response: {baz.foo_response}")
print(f"bar_response: {baz.bar_response}")
