import sys
from requests import ConnectionError


def try_request(function):
    def _inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ConnectionError:
            print("Opss, maybe you migth be without connection...")
            sys.exit(1)
    return _inner
