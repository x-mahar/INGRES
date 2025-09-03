# AI-driven ChatBOT for INGRES (MVP)

## 📌 Project Overview
This project aims to build an **AI-driven chatbot** for the **INGRES (India Ground Water Resource Estimation System)** platform.  
The chatbot will make it easier for users (researchers, planners, policymakers, and the public) to query **groundwater resource data**, view historical and current assessments, and gain insights without manually navigating complex datasets.

At this stage, we are working on the **Minimum Viable Prototype (MVP)**:
- Prepare and load sample groundwater dataset (2017–2020).
- Store it in **MongoDB** for easy access.
- Provide a backend API (Python/FastAPI) and later integrate a chatbot interface.

---

## 📂 Project Structure (MVP)

project_root/
│
├── data/ # Dataset directory
│ ├── GwaterExt2017-2020.csv # Groundwater extraction dataset (2017–2020)
│
├── scripts/
│ ├── insert_db.py # Script to insert CSV data into MongoDB
│
├── app/ # (Planned) Backend application code
│
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Tech Stack
- **Database:** MongoDB (local instance for MVP)
- **Backend:** Python (FastAPI planned)
- **Frontend:** To be added in later stages
- **Languages:** Python, Java (team mix)

---

## 📊 Dataset
- File: `GwaterExt2017-2020.csv`
- Content: Groundwater extraction records for India (2017–2020).
- Columns: State/UT, District, Block, Year, Recharge, Extraction, Stage, Category, etc.
- Source: Sample dataset prepared for MVP (not full official INGRES dataset).

---

## 🛠️ Setup Instructions

### 1️⃣ Install Requirements
- [Install MongoDB](https://www.mongodb.com/try/download/community) (default URI: `mongodb://localhost:27017`)
- Install Python libraries:
```bash
pip install pymongo pandas
2️⃣ Insert Data into MongoDB
Run the provided script to load the CSV dataset:

bash
Copy code
python scripts/insert_db.py
This will:

Connect to MongoDB at localhost:27017

Create a database: ingres_db

Create a collection: groundwater

Insert the CSV data as JSON documents

👨‍👩‍👦 Team Workflow
Each developer should run insert_db.py once to have the dataset locally.

Later, a shared MongoDB server can be used to avoid duplicate setup.

Even if teammates use different languages (Python, Java, etc.), all can query the same MongoDB dataset.