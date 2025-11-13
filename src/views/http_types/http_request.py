

class HttpRequest:
    def __init__(self, body: dict | None = None, param: dict | None = None) -> None:
        self.body = body or {}
        self.param = param or {}


'''
EX: HTTP Request class to encapsulate HTTP request detail
   e log information for debugging or monitoring purposes.

class HttpRequest:
    def __init__(
        self,
        body: dict | None = None,
        param: dict | None = None,
        url: str | None = None,
        method: str | None = None,
        headers: dict | None = None
    ) -> None:
        self.body = body
        self.param = param
        self.url = url
        self.method = method
        self.headers = headers

    def get_body(self) -> dict:
        return {
            "log": {
                "body": self.body,
                "param": self.param,
                "url": self.url,
                "method": self.method,
                "headers": self.headers
            }
        }

'''