import requests


class HTTPClient:

    def __init__(self):
        self._session = requests.Session()

    def request(self, method, url, **kwargs):
        with self._session.request(method, url, **kwargs) as rep:
            rep.encoding = 'utf-8'
        return rep
