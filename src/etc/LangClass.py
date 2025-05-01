import json
import sys
from types import SimpleNamespace

class langClass(object):

    def __init__(self, langCode):
        with open(f"./langPackages/{langCode}.json", encoding = "utf-8") as f:
            self.lang = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
