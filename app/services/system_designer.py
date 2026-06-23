def design_system(schema: dict):
    return {
        "architecture": "FastAPI + Services Layer",
        "components": schema["features"],
        "db": "PostgreSQL (planned)"
    }