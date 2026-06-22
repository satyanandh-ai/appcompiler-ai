def generate_schemas(design):

    ui_schema = {
        "pages": []
    }

    api_schema = {
        "endpoints": []
    }

    db_schema = {
        "tables": []
    }

    for page in design["pages"]:

        ui_schema["pages"].append({
            "name": page
        })

    for entity in design["entities"]:

        api_schema["endpoints"].append({
            "path": f"/api/{entity.lower()}",
            "method": "GET"
        })

        db_schema["tables"].append({
            "name": entity
        })

    return {
        "ui_schema": ui_schema,
        "api_schema": api_schema,
        "db_schema": db_schema
    }