def repair_schemas(schemas, errors):

    db = schemas["db_schema"]
    api = schemas["api_schema"]
    ui = schemas["ui_schema"]

    existing_tables = {t["name"] for t in db["tables"]}

    for error in errors:

        # Fix DB issue
        if "DB table" in error:
            table = "AutoFixedTable"
            if table not in existing_tables:
                db["tables"].append({"name": table})
                existing_tables.add(table)

        # Fix API missing
        if "No API endpoints" in error or "DB exists but no API layer" in error:
            api["endpoints"].append({
                "path": "/auto/fix",
                "method": "GET",
                "linked_table": "AutoFixedTable"
            })

        # Fix UI missing
        if "No UI pages" in error:
            ui["pages"].append({
                "name": "AutoFixPage",
                "route": "/auto"
            })

    return schemas