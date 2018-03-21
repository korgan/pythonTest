from pythontest import PythonTest


def test_function():
    client = PythonTest("token0123")
    assert client._runFunction(1) == 1


def test_function_fail():
    client = PythonTest("token0123")
    assert client._runFunction(0) is None


def test_request():
    client = PythonTest("token0123")
    assert client._runRequest("http://example.org") == 1


def test_request_404():
    client = PythonTest("token0123")
    assert client._runRequest("https://google.de/404") is None
