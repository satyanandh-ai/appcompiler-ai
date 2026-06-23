def extract_intent(text: str):
    return {
        "goal": text,
        "type": "app_building_request"
    }