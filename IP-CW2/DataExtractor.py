import json
import httpx
import pandas

class DataExtractor:
    #all document related functionalities
    def __init__(self, source):
        self.source = source
        self.df = None
        self.data = None

    def load(self):
        text = self.loadFromUrl()
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
            
    def loadFromUrl(self):
        try:
            response = httpx.get(self.source)
            response.raise_for_status()
            return response.text
        except httpx.RequestError:
            print("Failed to load - RequestError")
            return ""
        except httpx.HTTPStatusError:
            print("Failed to load - HTTPStatusError")
            return ""

    def verifyExtension(doc):
        pass

    def getContent(doc):
        pass
    