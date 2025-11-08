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
        print(loader.getContent("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))

if __name__ == "__main__":
    app = DocTracker()
    app.main()

