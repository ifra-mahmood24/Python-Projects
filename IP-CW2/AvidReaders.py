class AvidReaders:
    def __init__(self, df_copy):
        self.df_copy = df_copy

    #returns list of avid readers
    def getAvidReaders(self):
        reads = self.df_copy[self.df_copy["event_type"] == "pagereadtime"] #pageread.
        # replaces missing values with 0
        reads["event_readtime"] = reads["event_readtime"].fillna(0)
        total_time = reads.groupby("visitor_uuid")["event_readtime"].sum()
        return total_time.sort_values(ascending=False).head(10)

    def getTableOfReaders(lstAvidReaders):
        pass

        #returns a formatted display of list of avid readers
        #this function gets called in the display window of GUI