# 🧠 AI App Compiler System ⚙️

👨‍💻 Author: Satya Anandh  
🎯 Role: AI Engineer Intern Applicant  

---

## 📌 Overview 🚀

AI App Compiler System is a compiler-inspired AI pipeline that converts natural language requirements into structured, validated, and execution-ready application blueprints.

It transforms a single user prompt into a complete system definition including UI, API, and Database schemas with validation and execution simulation.

---

## ⚙️ Architecture Flow 🔁

User Prompt → Intent Extraction → System Design Layer → Schema Generation (UI / API / DB) → Validation Engine → Repair Engine → Execution Simulator → Final JSON Output

---

## 🧠 Core Idea 💡

Instead of treating LLMs as text generators, this system treats them as a **compiler frontend for software generation**, ensuring structured, consistent, and executable outputs.

---

## 🧩 Modules 🔧

🟡 Intent Extraction  
- Extracts app type and features from natural language input  

🟢 System Design Layer  
- Defines entities, roles, and pages  

🔵 Schema Generation  
- UI Schema → pages & layout  
- API Schema → endpoints & methods  
- DB Schema → tables & relationships  

🟣 Validation Engine  
- Ensures API ↔ DB consistency  
- Checks missing or invalid structures  
- Enforces cross-layer correctness  

🔴 Repair Engine  
- Fixes missing or inconsistent schema parts  
- Applies targeted repairs (not full regeneration)  

⚫ Execution Simulator  
- Generates runtime metadata  
- Counts DB tables, API endpoints, UI pages  

---

## 🧪 Example Input 📝

Build a CRM system with login, dashboard, contacts, and admin analytics

---

## 📤 Example Output 📦

```json
{
  "intent": {
    "app_type": "CRM",
    "features": ["login", "dashboard", "contacts"]
  },
  "design": {
    "entities": ["User", "Contact"],
    "roles": ["Admin", "User"],
    "pages": ["Login", "Dashboard", "Contacts"]
  },
  "schemas": {
    "ui_schema": {},
    "api_schema": {},
    "db_schema": {}
  },
  "validation": {
    "valid": true,
    "errors": []
  },
  "execution_trace": {
    "db_tables": 2,
    "api_endpoints": 2,
    "ui_pages": 3,
    "status": "compiler_run_complete"
  }
}

🚀 Tech Stack ⚙️

Python • FastAPI • Modular AI Pipeline • JSON Schema System • Rule-Based Validation & Repair

✨ Key Features ⭐

✔ Multi-stage AI compiler pipeline
✔ Cross-layer validation (UI ↔ API ↔ DB)
✔ Auto-repair system for inconsistencies
✔ Execution simulation layer
✔ Deterministic structured output

🚀 Run Instructions ▶️

pip install -r requirements.txt
uvicorn app.main:app --reload

Open: http://127.0.0.1:8000/

🧠 Key Insight 💡

This system reframes LLM-based application generation as a compiler problem instead of a prompt engineering problem, enabling structured, reliable, and execution-aware outputs.

👨‍💻 Author ✍️

Satya Anandh
AI Engineer Intern Applicant