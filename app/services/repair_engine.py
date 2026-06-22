def repair_schemas(schemas: dict):

    ui = schemas.get("ui_schema", {})
    api = schemas.get("api_schema", {})
    db = schemas.get("db_schema", {})

    ui_pages = {p["name"].lower() for p in ui.get("pages", [])}
    api_endpoints = {e["path"] for e in api.get("endpoints", [])}
    db_tables = {t["name"].lower() for t in db.get("tables", [])}

    repaired = schemas.copy()

    # -------------------------
    # 1. Fix missing UI schema
    # -------------------------
    if "ui_schema" not in repaired:
        repaired["ui_schema"] = {"pages": []}

    # -------------------------
    # 2. Fix missing API schema
    # -------------------------
    if "api_schema" not in repaired:
        repaired["api_schema"] = {"endpoints": []}

    # -------------------------
    # 3. Fix missing DB schema
    # -------------------------
    if "db_schema" not in repaired:
        repaired["db_schema"] = {"tables": []}

    # -------------------------
    # 4. Auto-repair missing DB tables from UI
    # -------------------------
    for page in ui_pages:
        if page not in db_tables:
            repaired["db_schema"]["tables"].append(
                {"name": page.capitalize()}
            )

    # -------------------------
    # 5. Auto-repair missing API endpoints from DB
    # -------------------------
    for table in db_tables:
        expected_endpoint = f"/api/{table}"
        if expected_endpoint not in api_endpoints:
            repaired["api_schema"]["endpoints"].append(
                {"path": expected_endpoint, "method": "GET"}
            )

    # -------------------------
    # Final output
    # -------------------------
    return repaired