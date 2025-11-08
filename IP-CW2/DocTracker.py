from DataExtractor import DataExtractor

class DocTracker:
    def __init__(self):
        self.df = None

    def main(self):
        #json_url = "http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_cw2.json"
        json_url = "http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_sample.json"


        loader = DataExtractor(json_url)
        df = loader.load()
        print(df)

if __name__ == "__main__":
    app = DocTracker()
    app.main()

