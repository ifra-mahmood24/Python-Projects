import json
import pandas

class DataExtractor:
    #all document related functionalities
    def __init__(self):
        self.df = None
        self.data = None

    def load(self, sourse):
        text = self.loadFromFile(sourse)
        self.data = self.parseJSON(text)
        self.df = pandas.DataFrame(self.data)
        return self.df
        
    def parseJSON(self, text):
        text = text.strip()
        if not text:
            return []
        try:
            lines = text.splitlines()
            parsedLines = [json.loads(line) for line in lines if line.strip()]
            return parsedLines
        except Exception:
            print("Failed to parse")
            return []
            
    def loadFromFile(self, source):
        try:
            with open(source, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print("Failed to load - File not found")
            return ""

    def verifyExtension(doc):
        pass

    def getContent(self, doc):
        return self.df[self.df["subject_doc_id"] == doc]
