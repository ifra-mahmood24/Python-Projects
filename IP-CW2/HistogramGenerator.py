import matplotlib.pyplot as plt
import numpy as np

class HistogramGenerator:

    @staticmethod
    def plot(data: dict, title: str, xlabel: str, ylabel: str):

        if data is None:
            print("No data to display")
            return

        # Convert pandas Series to dict
        if hasattr(data, "to_dict"):
            data = data.to_dict()

        if not isinstance(data, dict):
            data = dict(data)

        if len(data) == 0:
            print("No data available for histogram.")
            return

        labels = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(10, 5))
        plt.bar(labels, values)

        # Whole-number axis
        max_val = max(values)
        plt.yticks(np.arange(0, max_val + 1, 1))

        # Rotate labels for readability
        plt.xticks(rotation=90, ha="right")

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.tight_layout()
        plt.show()