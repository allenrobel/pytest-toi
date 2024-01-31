#!/usr/bin/env python

from typing import Any, Dict
from modules.baz import Baz

def test_monkeypatch_baz(monkeypatch) -> None:
    instance = Baz()

    def mock_foo_send_request(*args, **kwargs) -> Dict[str, Any]:
        return {"new_foo_response": 100}
    def mock_bar_send_request(*args, **kwargs) -> Dict[str, Any]:
        return {"new_bar_response": "b"}

    PATCH_PATH_FOO="modules.baz.Foo.send_request"
    PATCH_PATH_BAR="modules.baz.Bar.send_request"
    monkeypatch.setattr(PATCH_PATH_FOO, mock_foo_send_request)
    monkeypatch.setattr(PATCH_PATH_BAR, mock_bar_send_request)

    instance.do_something()
    assert instance.foo_response == {"new_foo_response": 100}
    assert instance.bar_response == {"new_bar_response": "b"}
