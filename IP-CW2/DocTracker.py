from DataExtractor import DataExtractor
from ViewByBrowser import ViewByBrowser
from AvidReaders import AvidReaders
from AlsoLikes import AlsoLikes

class DocTracker:
    def __init__(self):
        self.df = None

    def main(self):
        json_url = "./issuu_cw2.json"
        #json_url = "http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_sample.json"

        loader = DataExtractor(json_url)
        df = loader.load()
        print(df)
        print(loader.getContent("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))
        copy = df.copy()
        view = ViewByBrowser(copy)
        counts = view.getUserAgentCounts()
        print(counts)
        split = view.getBrowserCounts(counts)
        print(split)
        avid = AvidReaders(copy)
        r = avid.getAvidReaders()
        print(r)
        likes = AlsoLikes(copy)
        also_likes = likes.sort_alsoLikes("130716200231-1574c95da3c287d61e65f57e91f05085", likes.sort_func_count)
        print(also_likes)

        allowed = ["read", "pagereadtime", "pageread"]
        result = df[
            (df["visitor_uuid"] == "e1178362fc11d6ba") &
            (df["event_type"].isin(allowed))
        ][["ts", "event_type", "event_readtime"]]
        print(result.sort_values(by="ts"))

if __name__ == "__main__":
    app = DocTracker()
    app.main()

