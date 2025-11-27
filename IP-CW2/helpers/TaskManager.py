from analytics.ViewByBrowser import ViewByBrowser
from analytics.ViewByCountry import ViewByCountry
from analytics.AvidReaders import AvidReaders
from analytics.AlsoLikes import AlsoLikes
from GUI import GUI
from helpers.HistogramGenerator import HistogramGenerator

class TaskManager():
    def __init__(self):
        self.tasks = {
            "2a": self.task_2a,
            "2b": self.task_2b,
            "3a": self.task_3a,
            "3b": self.task_3b,
            "4": self.task_4,
            "5d": self.task_5d,
            "6": self.task_6,
            "7": self.task_7
        }

    def run_task(self, user_uuid, doc_uuid, task_id, df, file_name=""):
        handler = self.tasks.get(task_id)

        if not handler:
            print("Invalid task id")
            return
        
        return handler(user_uuid, doc_uuid, task_id, df, file_name)
    
    def require_doc(self, doc_uuid):
        if not doc_uuid:
            raise ValueError()

    # --- TASK HANDLERS --- #
    
    def task_2a(self, user_uuid, doc_uuid, df, file_name=""):
        v = ViewByCountry(df)
        self.require_doc(doc_uuid)
        countries = v.getCountryCounts(doc_uuid)
        HistogramGenerator.plot_helper(countries, f"Views by Country for {doc_uuid}", "Country", "Number of Views")
        return countries
    
    def task_2b(self, user_uuid, doc_uuid, df, file_name=""):
        v = ViewByCountry(df)
        self.require_doc(doc_uuid)
        countries = v.getCountryCounts(doc_uuid)
        continents = v.getContinentCounts(countries)
        HistogramGenerator.plot_helper(continents, f"Views by Continent for {doc_uuid}", "Continent", "Number of Views")
        return continents
    
    def task_3a(self, user_uuid, doc_uuid, df, file_name=""):
        vb = ViewByBrowser(df)
        user_agents = vb.getUserAgentCounts()
        HistogramGenerator.plot_helper(user_agents, "Browser Histogram", "Browser (Full User Agent)", "Number of Visitors")
        return user_agents
    
    def task_3b(self, user_uuid, doc_uuid, df, file_name=""):
        vb = ViewByBrowser(df)
        user_agents = vb.getUserAgentCounts()
        browsers = vb.getBrowserCounts(user_agents)
        HistogramGenerator.plot_helper(browsers, "Simplified Browser Histogram", "Browser Name", "Number of Visitors")
        return browsers
    
    def task_4(self, user_uuid, doc_uuid, df, file_name=""):
        ar = AvidReaders(df)
        return ar.getTableOfReaders(ar)
    
    def task_5d(self, user_uuid, doc_uuid, df, file_name=""):
        al = AlsoLikes(df)
        self.require_doc(doc_uuid)
        return al.sort_alsoLikes(doc_uuid, sort_func=al.sort_by_count_desc)
    
    def task_6(self, user_uuid, doc_uuid, df, file_name=""):
        self.require_doc(doc_uuid)
        al = AlsoLikes(df)
        also_likes = al.sort_alsoLikes(doc_uuid, sort_func=al.sort_by_count_desc)

        if len(also_likes) == 0:
            return "No related documents found.\n"

        try:
            al.displayGraph(doc_uuid, user_uuid)
            return also_likes
        except Exception as e:
            return f"Could not generate graph:\n{e}"

    def task_7(self, user_uuid, doc_uuid, df, file_name):
        GUI(
            preset_doc=doc_uuid,
            preset_user=user_uuid,
            preset_task="6",
            preset_file=file_name
        )
        return