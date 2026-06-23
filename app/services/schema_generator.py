def generate_schema(intent: dict):
    return {
        "entities": ["user", "auth", "database"],
        "features": ["login", "signup", "dashboard"]
    }