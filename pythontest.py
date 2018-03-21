import requests

__all__ = ('PythonTest')


class PythonTest(object):

    def __init__(self, token):
        self.token = token

    def _runFunction(self, input):
        if input == 1:
            return 1
        return None

    def _runRequest(self, url):
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return 1

        return None
