from modules.aaa import AAA

class Foo:
    def __init__(self):
        self.aaa = AAA()
    def send_request(self):
        return self.aaa.send_rest_request("foo")
