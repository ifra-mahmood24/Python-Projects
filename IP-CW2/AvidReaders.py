class AvidReaders:
    def __init__(self):
        pass


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