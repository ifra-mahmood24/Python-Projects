import graphviz
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import graphviz
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
class AlsoLikes:
    read_events = ["pageread", "pagereadtime", "read"]
>>>>>>> Stashed changes


    def getReaders(self, doc_UUID):
        readers = self.df_copy[
            (self.df_copy["subject_doc_id"] == doc_UUID) &
            (self.df_copy["event_type"].isin(self.read_events))
        ]
        return readers["visitor_uuid"].unique()
    
    def getDocs(self, visitor_UUID):
        docs = self.df_copy[
            (self.df_copy["visitor_uuid"] == visitor_UUID) &
            (self.df_copy["event_type"].isin(self.read_events))
        ]
        return docs["subject_doc_id"].unique()

    def sort_by_common_readers(self, item):
        doc_id, count = item # item is a tuple (doc_id, count)
        return -count      # negative for descending order

    def sort_by_doc_if(self, item):
        doc_id, count = item
        return doc_id
    
    def sort_by_least_common(self, item):
        doc_id, count = item
        return count

    def alsoLikes(self, doc_UUID, sort_func, visitor_UUID = ""):
        if sort_func is None:     # use internal function if none supplied
            sort_func = self.sort_by_common_readers
        
        lst_readers = self.getReaders(doc_UUID)
        doc_counts = {}
        
        for reader in lst_readers:
            lst_docs = self.getDocs(reader)
            for doc in lst_docs:
                if doc != doc_UUID:
                    doc_counts[doc] = doc_counts.get(doc, 0) + 1
        return sorted(doc_counts.items(), key = sort_func)

    def displayGraph(self, docuuid, visuuid="", topN=10):
        from GraphGenerator import GraphGenerator
        
        results = self.alsoLikes(docuuid)
        likedDocs = [doc for doc, _ in results[:topN]]

        gg = GraphGenerator(self.df_copy)
        dotFile = gg.write_dot_file(
            main_doc=docuuid,
            liked_docs=likedDocs,
            highlight_reader=visuuid,
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

