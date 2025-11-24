import graphviz
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class AlsoLikes:
    def __init__(self, df_copy):
        self.df_copy = df_copy

    read_events = ["pageread", "pagereadtime", "read"] #events identifying the readers 

    def getReaders(self, doc_UUID):
        readers = self.df_copy[
            (self.df_copy["subject_doc_id"] == doc_UUID) &
            (self.df_copy["event_type"].isin(self.read_events))
        ]
        return readers["visitor_uuid"].dropna().unique()
    
    def getDocs(self, visitor_UUID):
        docs = self.df_copy[
            (self.df_copy["visitor_uuid"] == visitor_UUID) &
            (self.df_copy["event_type"].isin(self.read_events))
        ]
        return docs["subject_doc_id"].dropna().unique()

    def sort_by_count_desc(self, item):
        doc, count = item
        return -count  # highest count first

    def sort_by_count_asc(self, item):
        doc, count = item
        return count  # lowest first

    def sort_by_doc_id(self, item):
        doc, count = item
        return doc  # alphabetical

    def compute_alsoLikes(self, doc_UUID):
        doc_counts = {}
        readers = self.getReaders(doc_UUID)

        for reader in readers:
            docs = self.getDocs(reader)
            for d in docs:
                if d != doc_UUID:
                    doc_counts[d] = doc_counts.get(d, 0) + 1
        
        return list(doc_counts.items())  # return list of (doc, count)
    
    def sort_alsoLikes(self, doc_UUID, sort_func=None, visitor_UUID=""):
        if sort_func is None:
            sort_func = self.sort_by_count_desc  # default for Task 5d

        pairs = self.compute_alsoLikes(doc_UUID)
        sorted_pairs = sorted(pairs, key=sort_func)
        # create a list of top 10 docs
        return [doc for doc, _ in sorted_pairs[:10]]

    def displayGraph(self, doc_UUID, visitor_UUID=""):
        from ..generators_helpers.GraphGenerator import GraphGenerator

        likedDocs = self.sort_alsoLikes(doc_UUID)

        gg = GraphGenerator(self.df_copy)
        dotFile = gg.write_dot_file(
            main_doc=doc_UUID,
            liked_docs=likedDocs,
            highlight_reader=visitor_UUID,
            filename="also_likes.dot"
        )

        graph = graphviz.Source.from_file(dotFile)
        png_path = "also_likes.png"
        graph.render(filename="also_likes", format="png", cleanup=True)

        img = mpimg.imread(png_path)
        plt.figure(figsize=(10,10))
        plt.imshow(img)
        plt.axis("off")
        plt.title("Also Likes Graph")
        plt.show()

