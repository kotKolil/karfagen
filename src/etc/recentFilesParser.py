import json

class recentFilesParser:

    def __init__(self):
        self.data = json.load(open("./jdata/recentFiles.json", encoding="UTF-8"))

    def addFile(self, filename):
        self.data["recentFiles"].append(filename)
        with open("./jdata/recentFiles.json", "w") as file:
            json.dump(self.data, file, indent=4)
            file.close()