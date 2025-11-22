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

    def getTableOfReaders(self, series=None):
        if series is None:
            series = self.getAvidReaders()
        
        
        lines = []
        header = f"{'Rank':<5} {'Visitor UUID': <40} {'Total Time:':>10}"
        lines.append(header)
        lines.append("-" * len(header))

        for i, (uuid, total) in enumerate(series.items(), start=1):
            lines.append(f"{i:<5} {uuid:<40} {int(total):>10}")

        return "\n".join(lines)


    def getAvidReaders(docID):
        pass
        #returns list of avid readers

    def getTableOfReaders(self, series=None):
        if series is None:
            series = self.getAvidReaders()
        
        
        lines = []
        header = f"{'Rank':<5} {'Visitor UUID': <40} {'Total Time:':>10}"
        lines.append(header)
        lines.append("-" * len(header))

        for i, (uuid, total) in enumerate(series.items(), start=1):
            lines.append(f"{i:<5} {uuid:<40} {int(total):>10}")

        return "\n".join(lines)

        #returns a formatted display of list of avid readers
        #this function gets called in the display window of GUI