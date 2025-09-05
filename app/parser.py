import re
from typing import Dict, Any
from database import DatabaseHelper
from difflib import get_close_matches


class QueryParser:
    def __init__(self):
        self.db = DatabaseHelper()

        # Load possible values from DB
        self.states = [s for s in self.db.get_all_states()]
        self.statuses = [s for s in self.db.get_status_categories()]
        self.years = [str(y) for y in self.db.get_available_years()]
        print("States loaded from DB:", self.states)

    def parse_query(self, query: str) -> Dict[str, Any]:

        parsed: Dict[str, Any] = {}
        q_lower = query.lower()

        # Year range (2017, 2020 / 2017-2020)
        range_match = re.search(r"(\d{4})\s*(?:to|-)\s*(\d{4})", q_lower)
        if range_match:
            parsed["year_from"] = int(range_match.group(1))
            parsed["year_to"] = int(range_match.group(2))
        else:
            #Single year
            year_match = re.search(r"\b(19\d{2}|20\d{2})\b", q_lower)
            if year_match:
                parsed["year"] = int(year_match.group(1))

        #State (case-insensitive exact match)
        for state in self.states:
            if state.lower() in q_lower:   # always lowercase compare
                parsed["state"] = state    # keep DB spelling
                break

        #Fuzzy match fallback
        if "state" not in parsed:
            match = get_close_matches(q_lower, [s.lower() for s in self.states], n=1, cutoff=0.7)
            if match:
                idx = [s.lower() for s in self.states].index(match[0])
                parsed["state"] = self.states[idx]

        #Status (case-insensitive)
        for status in self.statuses:
            if status and status.lower() in q_lower:
                parsed["status"] = status
                break

        if "status" not in parsed:
            match = get_close_matches(q_lower, [s.lower() for s in self.statuses], n=1, cutoff=0.7)
            if match:
                idx = [s.lower() for s in self.statuses].index(match[0])
                parsed["status"] = self.statuses[idx]

        return parsed


if __name__ == "__main__":
    parser = QueryParser()
    print("Ask me about groundwater (type 'exit' to quit)")
    print("Examples:")
    print("  'Show groundwater of Andhra Pradesh in 2020'")
    print("  'Groundwater status in Punjab from 2017 to 2020'")

    while True:
        q = input("\nYour query > ")
        if q.lower() in ["exit", "quit"]:
            print("Goodbye")
            break

        parsed = parser.parse_query(q)
        print("Parsed query:", parsed)

        if parsed:
            results = parser.db.query_groundwater_data(parsed)
            if results:
                print("Results:")
                for r in results:
                    print(r)
            else:
                print("No data found.")
        else:
            print("Could not understand your query.")
