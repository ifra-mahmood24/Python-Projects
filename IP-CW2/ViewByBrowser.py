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

    def displayHistogram():
        pass