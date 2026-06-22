def validate_schemas(schemas):

    errors = []

    db_tables = {t["name"] for t in schemas["db_schema"]["tables"]}
    api_endpoints = schemas["api_schema"]["endpoints"]
    ui_pages = schemas["ui_schema"]["pages"]

    # API → DB consistency check
    for api in api_endpoints:
        table = api.get("linked_table")
        if table and table not in db_tables:
            errors.append(f"API references missing DB table: {table}")

    # UI must exist
    if len(ui_pages) == 0:
        errors.append("No UI pages defined")

    # API must exist
    if len(api_endpoints) == 0:
        errors.append("No API endpoints defined")

    # DB without API = design issue
    if len(db_tables) > 0 and len(api_endpoints) == 0:
        errors.append("DB exists but no API layer")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }