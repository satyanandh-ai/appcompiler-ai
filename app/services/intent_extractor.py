from app.models.schemas import Intent


def extract_intent(user_prompt: str):

    prompt = user_prompt.lower()

    features = []

    keywords = [
        "login",
        "dashboard",
        "contacts",
        "payments",
        "analytics"
    ]

    for item in keywords:
        if item in prompt:
            features.append(item)

    return Intent(
        app_type="CRM",
        features=features
    )