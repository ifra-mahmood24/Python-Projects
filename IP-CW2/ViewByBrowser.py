import matplotlib.pyplot as plt
import numpy as np
class ViewByBrowser:
    def __init__(self, df_copy):
        self.df_copy = df_copy

    def getUserAgentCounts(self):
        return self.df_copy["visitor_useragent"].astype(str).value_counts()
    
    def getBrowserCounts(self, counts):
        browser_counts = {}
        for user_agent, count in counts.items():
            browser = user_agent.split("/", 1)[0]
            browser_counts[browser] = browser_counts.get(browser, 0) + count
        return browser_counts

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

        max_val = max(values)
        plt.yticks(np.arange(0, max_val + 1, 1))
        plt.xticks(rotation=90)
        plt.xlabel("Continent")
        plt.ylabel("Number of Visitors")
        plt.title(title)
        plt.tight_layout()
        plt.show()