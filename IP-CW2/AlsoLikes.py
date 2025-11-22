class AlsoLikes:
    read_events = ["pageread", "pagereadtime"]

    def __init__(self, df_copy):
        self.df_copy = df_copy

    def getReaders(self, doc_UUID):
        readers = self.df_copy[(self.df_copy["subject_doc_id"] == doc_UUID)] # & (self.df_copy["event_type"].isin(self.read_events))
        return readers["visitor_uuid"].unique()
    
    def getDocs(self, visitor_UUID):
        docs = self.df_copy[(self.df_copy["visitor_uuid"] == visitor_UUID)]
        return docs["subject_doc_id"].unique()

    # def sort_func():
    #     lstSortedDoc = []

    #     if readersOfDoc1 == readersOfMainDoc:
    #         lstSortedDoc.append(doc1)

    def alsoLikes(self, doc_UUID, sort_func, visitor_UUID = ""):
        lst_readers = self.getReaders(doc_UUID)
        doc_counts = {}
        
        for reader in lst_readers:
            lst_docs = self.getDocs(reader)
            for doc in lst_docs:
                if doc != doc_UUID:
                    doc_counts[doc] = doc_counts.get(doc, 0) + 1
        return sorted(doc_counts.items(), key = sort_func)

    def displayGraph():
        pass
