import matplotlib.pyplot as plt
import numpy as np
class ViewByCountry:
    def __init__(self, df_copy):
        self.df_copy = df_copy

        # Map ISO country codes to continent codes
        self.continent_map = {
        # Africa
        "DZ": "AF", "AO": "AF", "BJ": "AF", "BW": "AF", "BF": "AF", "BI": "AF", "CM": "AF",
        "CV": "AF", "CF": "AF", "TD": "AF", "KM": "AF", "CD": "AF", "CG": "AF", "DJ": "AF",
        "EG": "AF", "GQ": "AF", "ER": "AF", "ET": "AF", "GA": "AF", "GM": "AF", "GH": "AF",
        "GN": "AF", "GW": "AF", "CI": "AF", "KE": "AF", "LS": "AF", "LR": "AF", "LY": "AF",
        "MG": "AF", "MW": "AF", "ML": "AF", "MR": "AF", "MU": "AF", "YT": "AF", "MA": "AF",
        "MZ": "AF", "NA": "AF", "NE": "AF", "NG": "AF", "RE": "AF", "RW": "AF", "SH": "AF",
        "ST": "AF", "SN": "AF", "SC": "AF", "SL": "AF", "SO": "AF", "ZA": "AF", "SS": "AF",
        "SD": "AF", "SZ": "AF", "TZ": "AF", "TG": "AF", "TN": "AF", "UG": "AF", "EH": "AF",
        "ZM": "AF", "ZW": "AF",

        # Antarctica
        "AQ": "AN",

        # Asia
        "AF": "AS", "AM": "AS", "AZ": "AS", "BH": "AS", "BD": "AS", "BT": "AS", "BN": "AS",
        "KH": "AS", "CN": "AS", "CY": "AS", "GE": "AS", "HK": "AS", "IN": "AS", "ID": "AS",
        "IR": "AS", "IQ": "AS", "IL": "AS", "JP": "AS", "JO": "AS", "KZ": "AS", "KP": "AS",
        "KR": "AS", "KW": "AS", "KG": "AS", "LA": "AS", "LB": "AS", "MO": "AS", "MY": "AS",
        "MV": "AS", "MN": "AS", "MM": "AS", "NP": "AS", "OM": "AS", "PK": "AS", "PS": "AS",
        "PH": "AS", "QA": "AS", "SA": "AS", "SG": "AS", "LK": "AS", "SY": "AS", "TW": "AS",
        "TJ": "AS", "TH": "AS", "TR": "AS", "TM": "AS", "AE": "AS", "UZ": "AS", "VN": "AS",
        "YE": "AS",

        # Europe
        "AL": "EU", "AD": "EU", "AT": "EU", "BY": "EU", "BE": "EU", "BA": "EU", "BG": "EU",
        "HR": "EU", "CY": "EU", "CZ": "EU", "DK": "EU", "EE": "EU", "FO": "EU", "FI": "EU",
        "FR": "EU", "DE": "EU", "GI": "EU", "GR": "EU", "GG": "EU", "VA": "EU", "HU": "EU",
        "IS": "EU", "IE": "EU", "IM": "EU", "IT": "EU", "JE": "EU", "LV": "EU", "LI": "EU",
        "LT": "EU", "LU": "EU", "MT": "EU", "MD": "EU", "MC": "EU", "ME": "EU", "NL": "EU",
        "MK": "EU", "NO": "EU", "PL": "EU", "PT": "EU", "RO": "EU", "RU": "EU", "SM": "EU",
        "RS": "EU", "SK": "EU", "SI": "EU", "ES": "EU", "SE": "EU", "CH": "EU",
        "UA": "EU", "GB": "EU",

        # North America
        "AG": "NA", "BS": "NA", "BB": "NA", "BZ": "NA", "CA": "NA", "CR": "NA", "CU": "NA",
        "DM": "NA", "DO": "NA", "SV": "NA", "GD": "NA", "GT": "NA", "HT": "NA", "HN": "NA",
        "JM": "NA", "MX": "NA", "NI": "NA", "PA": "NA", "KN": "NA", "LC": "NA", "VC": "NA",
        "TT": "NA", "US": "NA",

        # Oceania
        "AS": "OC", "AU": "OC", "CK": "OC", "FJ": "OC", "PF": "OC", "GU": "OC", "KI": "OC",
        "MH": "OC", "FM": "OC", "NR": "OC", "NC": "OC", "NZ": "OC", "NU": "OC", "NF": "OC",
        "PW": "OC", "PG": "OC", "WS": "OC", "SB": "OC", "TK": "OC", "TO": "OC", "TV": "OC",
        "VU": "OC", "WF": "OC",

        # South America
        "AR": "SA", "BO": "SA", "BR": "SA", "CL": "SA", "CO": "SA", "EC": "SA", "FK": "SA",
        "GF": "SA", "GY": "SA", "PY": "SA", "PE": "SA", "SR": "SA", "UY": "SA", "VE": "SA"
    }

    # ---------- Task 2a ----------
    def getCountryCounts(self, doc_id):
        subset = self.df_copy[self.df_copy["subject_doc_id"] == doc_id]
        if subset.empty:
            return {}
        return subset["visitor_country"].astype(str).value_counts()

    # ---------- Task 2b ----------
    def getContinentCounts(self, country_counts):
        continents = {}
        for code, count in country_counts.items():
            continent = self.continent_map.get(code, "Unknown")
            continents[continent] = continents.get(continent, 0) + count
        return continents

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

        plt.figure(figsize=(10, 5))
        plt.bar(labels, values)

        max_val = max(values)
        plt.yticks(np.arange(0, max_val + 1, 1))
        plt.xticks(rotation=90)
        plt.xlabel("Country")
        plt.ylabel("Number of Views")
        plt.title(title)
        plt.tight_layout()
        plt.show()