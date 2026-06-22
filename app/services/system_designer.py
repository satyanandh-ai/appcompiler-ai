def generate_design(intent):

    design = {
        "entities": [],
        "roles": ["Admin", "User"],
        "pages": []
    }

    if "contacts" in intent.features:
        design["entities"].append("Contact")
        design["pages"].append("Contacts")

    if "dashboard" in intent.features:
        design["pages"].append("Dashboard")

    if "login" in intent.features:
        design["entities"].append("User")
        design["pages"].append("Login")

    return design