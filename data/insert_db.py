from pymongo import MongoClient, ASCENDING
import json

client = MongoClient("mongodb://localhost:27017")
db = client["ingres_bot"]
col = db["groundwater_state"]

# Unique index on (state, year)
col.create_index([("state", ASCENDING), ("year", ASCENDING)], unique=True)

# Load NDJSON and upsert
with open("data/groundwater_state_2017_2020.ndjson", "r", encoding="utf-8") as f:
    for line in f:
        doc = json.loads(line)
        col.update_one({"state": doc["state"], "year": doc["year"]}, {"$set": doc}, upsert=True)
