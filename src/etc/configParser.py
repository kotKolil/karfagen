import json

from src.GUI.styles.WhiteTheme import *
from src.GUI.styles.ConsoleTheme import *
from src.GUI.styles.DarkTheme import *
from src.GUI.styles.SepiaTheme import *


class configParser:

    def __init__(self, config_name="./jdata/config.json", encoding="utf-8"):
        self.data = json.load(open(config_name, encoding=encoding))

        self.APP_THEME = None
        self.APP_THEME_CSS = None
        self.WINDOW_NAME = self.data["WINDOW_NAME"]
        self.TEXT_SIZE = self.data["TEXT_SIZE"]
        self.FONT_NAME = self.data["FONT_NAME"]
        self.WINDOW_STYLE = self.data["WINDOW_STYLE"]
        self.APP_THEME = self.data["APP_THEME"]
        self.APP_THEME_NAME = self.data["APP_THEME"]
        self.OPACITY_WINDOWS = self.data["OPACITY_WINDOWS"]
        self.WINDOW_WIDTH = self.data["WINDOW_WIDTH"]
        self.WINDOW_HEIGHT = self.data["WINDOW_HEIGHT"]
        self.APP_THEME = self.data["APP_THEME"]
        self.langCode = self.data["langCode"]
        match self.APP_THEME:
            case "white":
                self.APP_THEME_CSS = WhiteTheme.style
            case "dark":
                self.APP_THEME_CSS = DarkTheme.style
            case "console":
                self.APP_THEME_CSS = ConsoleTheme.style
            case "sepia":
                self.APP_THEME_CSS = SepiaTheme.style

    def save(self):
        data = {
            "WINDOW_NAME": self.WINDOW_NAME,
            "TEXT_SIZE": self.TEXT_SIZE,
            "FONT_NAME": self.FONT_NAME,
            "WINDOW_STYLE": self.WINDOW_STYLE,
            "APP_THEME": self.APP_THEME,
            "WINDOW_WIDTH": self.WINDOW_WIDTH,
            "WINDOW_HEIGHT": self.WINDOW_HEIGHT,
            "OPACITY_WINDOWS" : self.OPACITY_WINDOWS,
            "langCode": self.langCode
        }
        with open("./jdata/config.json", "w") as file:
            json.dump(data, file, indent=4)
            file.close()