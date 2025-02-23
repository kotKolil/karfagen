import json

from src.styles.WhiteTheme import *
from src.styles.ConsoleTheme import *
from src.styles.DarkTheme import *
class configParser():

    def __init__(self, configName = "./jsonData/config.json", encoding = "utf-8"):
        self.data = json.load(open(configName, "r", encoding = encoding))

        self.WINDOW_NAME = self.data["WINDOW_NAME"]
        self.TEXT_SIZE = self.data["TEXT_SIZE"]
        self.FONT_NAME = self.data["FONT_NAME"]
        self.WINDOW_STYLE = self.data["WINDOW_STYLE"]
        self.APP_THEME = self.data["APP_THEME"]
        match self.APP_THEME:
            case "white":
                self.APP_THEME = WhiteTheme.style
            case "dark":
                self.APP_THEME = DarkTheme.style
            case "console":
                self.APP_THEME = ConsoleTheme.style

    def save(self):
        data = {
            "WINDOW_NAME": self.WINDOW_NAME,
            "TEXT_SIZE": self.TEXT_SIZE,
            "FONT_NAME": self.FONT_NAME,
            "WINDOW_STYLE": self.WINDOW_STYLE,
            "APP_THEME": self.APP_THEME,
        }
        with open("./jsonData/config.json", "w") as file:
            json.dump(data, file, indent=4)
            file.close()