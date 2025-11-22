import matplotlib.pyplot as plt

class ViewByBrowser:
    def __init__(self):
        pass

    def getBroswer():
        pass
        #format the browser part from the visitor_useragent

    def displayHistogram(self, data, title="Histogram"):
        if data is None:
            print("No data to display")
            return
        
        if hasattr(data, "to_dict"):
            data = data.to_dict()

        if not isinstance(data, dict):
            try:
                data = dict(data)
            except Exception:
                print("Could not convert data to dictionary for histogram")

        if len(data) == 0:
            print("No data to display")

        labels = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(10,5))
        plt.bar(labels, values)
        plt.xticks(rotation=90)
        plt.title(title)
        plt.tight_layout()
        plt.show()