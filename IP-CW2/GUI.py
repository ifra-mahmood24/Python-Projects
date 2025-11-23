import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from DataExtractor import DataExtractor
from ViewByBrowser import ViewByBrowser
from ViewByCountry import ViewByCountry
from AvidReaders import AvidReaders
from AlsoLikes import AlsoLikes
from GraphGenerator import GraphGenerator


class GUI:
    def __init__(self, preset_doc=None, preset_user=None,preset_task=None, preset_file=None):
        self.df = None  # dataframe loaded after browsing or URL load

        self.window = tk.Tk()
        self.window.title("Document Tracker")
        self.window.geometry("600x550")

        # ------------------ TOP INPUT SECTION ------------------
        frame_top = tk.Frame(self.window)
        frame_top.pack(pady=10)

        # Document ID
        tk.Label(frame_top, text="Document UUID:").grid(row=0, column=0, sticky="w")
        self.doc_entry = tk.Entry(frame_top, width=45)
        self.doc_entry.grid(row=0, column=1, padx=5, pady=3)
        if preset_doc:
            self.doc_entry.insert(0, preset_doc)

        # User ID
        tk.Label(frame_top, text="User UUID:").grid(row=1, column=0, sticky="w")
        self.user_entry = tk.Entry(frame_top, width=45)
        self.user_entry.grid(row=1, column=1, padx=5, pady=3)
        if preset_user:
            self.user_entry.insert(0, preset_user)

        # Task selection dropdown
        tk.Label(frame_top, text="Select Task:").grid(row=2, column=0, sticky="w")

        self.task_var = tk.StringVar()
        self.task_dropdown = ttk.Combobox(
            frame_top, textvariable=self.task_var, width=42,
            values=["2a - Views by Country",
                    "2b - Views by Continent",
                    "3a - Browser Histogram",
                    "3b - Simplified Browser Histogram",
                    "4 - Top 10 Avid Readers",
                    "5d - Also Likes Top 10",
                    "6 - Generate Also-Likes Graph"]
        )
        self.task_dropdown.grid(row=2, column=1, padx=5, pady=3)
        if preset_task:
            self.task_dropdown.set(preset_task)

        # ------------------ DATA LOAD SECTION ------------------
        frame_data = tk.Frame(self.window)
        frame_data.pack(pady=10)

        tk.Label(frame_data, text="Load Data from File:").grid(row=0, column=0, sticky="w")

        self.url_entry = tk.Entry(frame_data, width=45)
        self.url_entry.grid(row=0, column=1, padx=5, pady=3)
        if preset_file:
            self.url_entry.insert(0, preset_file)

        browse_btn = tk.Button(frame_data, text="Browse",
                               command=self.browse_file)
        browse_btn.grid(row=0, column=2, padx=5)

        load_btn = tk.Button(frame_data, text="Load Data",
                             command=self.load_data)
        load_btn.grid(row=1, column=1, pady=5)

        # ------------------ OUTPUT BOX ------------------
        frame_output = tk.Frame(self.window)
        frame_output.pack(pady=10, fill="both", expand=True)

        tk.Label(frame_output, text="Output:").pack(anchor="w")

        self.output_box = tk.Text(frame_output, height=15, width=70)
        self.output_box.pack(fill="both", expand=True)

        # ------------------ RUN BUTTON ------------------
        run_btn = tk.Button(self.window, text="Run Task", command=self.run_task)
        run_btn.pack(pady=10)

        self.window.mainloop()

    # -----------------------------------------------------
    #                   BUTTON FUNCTIONS
    # -----------------------------------------------------

    def browse_file(self):
        filepath = filedialog.askopenfilename(
            title="Select JSON file", filetypes=[("JSON files", "*.json")]
        )
        if filepath:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filepath)

    def load_data(self):
        path = self.url_entry.get().strip()
        if not path:
            messagebox.showerror("Error", "Please enter a URL or choose a file.")
            return

        try:
            loader = DataExtractor(path)
            self.df = loader.load()
            messagebox.showinfo("Success", "Data loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data:\n{e}")

    def run_task(self):
        if self.df is None:
            messagebox.showerror("Error", "Load data first.")
            return

        task = self.task_var.get()
        doc = self.doc_entry.get().strip()
        user = self.user_entry.get().strip()

        v_country = ViewByCountry(self.df)
        v_browser = ViewByBrowser(self.df)
        avid = AvidReaders(self.df)
        al = AlsoLikes(self.df)

        self.output_box.delete("1.0", tk.END)

        # ---------------- TASK LOGIC -----------------------

        if "2a" in task:
            if not doc:
                return self.need_doc()
            counts = v_country.getCountryCounts(doc)
            self.output_box.insert(tk.END, str(counts))
            v_country.displayHistogram(counts, f"Views by Country for {doc}")

        elif "2b" in task:
            if not doc:
                return self.need_doc()
            counts = v_country.getCountryCounts(doc)
            cont = v_country.getContinentCounts(counts)
            self.output_box.insert(tk.END, str(cont))
            v_country.displayHistogram(cont, f"Views by Continent for {doc}")

        elif "3a" in task:
            counts = v_browser.getUserAgentCounts()
            self.output_box.insert(tk.END, str(counts))
            v_browser.displayHistogram(counts, "Browser Histogram")

        elif "3b" in task:
            counts = v_browser.getUserAgentCounts()
            simple = v_browser.getBrowserCounts(counts)
            self.output_box.insert(tk.END, str(simple))
            v_browser.displayHistogram(simple, "Simplified Browser Histogram")

        elif "4" in task:
            table = avid.getTableOfReaders()
            self.output_box.insert(tk.END, str(table))

        elif "5d" in task:
            if not doc:
                return self.need_doc()
            results = al.sort_alsoLikes(doc) 
            self.output_box.insert(tk.END, "Top 10 Also-Likes:\n\n")
            for d, c in results:
                self.output_box.insert(tk.END, f"{d}   ({c} shared readers)\n")

        elif "6" in task:
            if not doc:
                return self.need_doc()

            al = AlsoLikes(self.df)
            results = al.sort_alsoLikes(doc)

            if len(results) == 0:
                self.output_box.insert(tk.END, "No related documents found.\n")
                messagebox.showinfo("No Results", "No 'also-like' documents found for this ID.")
                return

            try:
                al.displayGraph(doc, user)
            except Exception as e:
                messagebox.showerror("Graph Error", f"Could not generate graph:\n{e}")
                print(e)


    def need_doc(self):
        messagebox.showerror("Error", "Document UUID is required for this task.")