#!/usr/bin/env python
from modules.foo import Foo
from modules.bar import Bar

class Baz:
    """
    class under test
    """
    def __init__(self):
        self.foo = Foo()
        self.bar = Bar()
    def do_something(self):
        self.foo_response = self.foo.send_request()
        self.bar_response = self.bar.send_request()
