from pymongo import MongoClient
from typing import List, Dict


class DatabaseHelper:
    def __init__(self, db_uri="mongodb://localhost:27017/", db_name="ingres_bot",
                 collection_name="groundwater_state"):
        """Initialize MongoDB connection"""
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def query_groundwater_data(self, params: Dict[str, str]) -> List[Dict]:
        """
        Filter data using state, status, year, or year range.
        Supported keys: state, block, status, year, year_from, year_to
        """
        query = {}

        # Match state
        if "state" in params and params["state"]:
            query["state"] = params["state"]

        # Match block (if you ever add block-level data)
        if "block" in params and params["block"]:
            query["block"] = params["block"]

        # Match status
        if "status" in params and params["status"]:
            query["status"] = params["status"]

        # Match single year
        if "year" in params and params["year"]:
            query["year"] = int(params["year"])

        # Match year range
        if "year_from" in params or "year_to" in params:
            year_query = {}
            if "year_from" in params:
                year_query["$gte"] = int(params["year_from"])
            if "year_to" in params:
                year_query["$lte"] = int(params["year_to"])
            query["year"] = year_query

        cursor = self.collection.find(query)
        # Strip MongoDB internal `_id` field
        return [{k: v for k, v in doc.items() if k != "_id"} for doc in cursor]

    def get_all_states(self) -> List[str]:
        """Get all unique states"""
        return self.collection.distinct("state")

    def get_status_categories(self) -> List[str]:
        """Get all unique status categories"""
        return self.collection.distinct("status")

    def get_available_years(self) -> List[int]:
        """Get all available years"""
        return self.collection.distinct("year")

    def close(self):
        """Close DB connection"""
        self.client.close()


# Helper function to get DatabaseHelper instance
def get_database_helper():
    return DatabaseHelper()
