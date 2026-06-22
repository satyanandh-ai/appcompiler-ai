def validate_schemas(schemas: dict):

    errors = []
    warnings = []

    ui = schemas.get("ui_schema", {})
    api = schemas.get("api_schema", {})
    db = schemas.get("db_schema", {})

    ui_pages = {p["name"].lower() for p in ui.get("pages", [])}
    api_endpoints = {e["path"] for e in api.get("endpoints", [])}
    db_tables = {t["name"].lower() for t in db.get("tables", [])}

    # -------------------------
    # 1. UI ↔ DB consistency
    # -------------------------
    for page in ui_pages:
        if page not in db_tables:
            warnings.append(f"UI page '{page}' has no matching DB table")

    # -------------------------
    # 2. API ↔ DB consistency
    # -------------------------
    for endpoint in api_endpoints:
        clean = endpoint.replace("/api/", "").lower()
        if clean not in db_tables:
            warnings.append(f"API endpoint '{endpoint}' has no DB mapping")

    # -------------------------
    # 3. Missing core schema checks
    # -------------------------
    if not ui_pages:
        errors.append("UI schema has no pages")

    if not api_endpoints:
        errors.append("API schema has no endpoints")

    if not db_tables:
        errors.append("DB schema has no tables")

    # -------------------------
    # Final result
    # -------------------------
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }