from modules.aaa import AAA

class Bar(AAA):
    def __init__(self):
        super().__init__()
    def send_request(self):
        return self.send_rest_request("bar")
