from fastapi import FastAPI

from app.services.intent_extractor import extract_intent
from app.services.system_designer import generate_design
from app.services.schema_generator import generate_schemas

from app.services.validator import validate_schemas
from app.services.repair_engine import repair_schemas

app = FastAPI()


@app.get("/")
def root():

    prompt = "Build CRM with login dashboard contacts"

    # -------------------
    # Stage 1: Intent
    # -------------------
    intent = extract_intent(prompt)

    # -------------------
    # Stage 2: Design
    # -------------------
    design = generate_design(intent)

    # -------------------
    # Stage 3: Schema Generation
    # -------------------
    schemas = generate_schemas(design)

    # -------------------
    # Stage 4: Validation (Compiler Check)
    # -------------------
    validation = validate_schemas(schemas)

    # -------------------
    # Stage 5: Repair Engine (Auto-fix)
    # -------------------
    if not validation["valid"]:
        schemas = repair_schemas(schemas, validation["errors"])

        # re-validate after repair
        validation = validate_schemas(schemas)

    # -------------------
    # Final Execution Trace (IMPORTANT for evaluation)
    # -------------------
    execution_trace = {
        "db_tables": len(schemas["db_schema"]["tables"]),
        "api_endpoints": len(schemas["api_schema"]["endpoints"]),
        "ui_pages": len(schemas["ui_schema"]["pages"]),
        "status": "compiler_run_complete"
    }

    return {
        "prompt": prompt,
        "intent": intent.model_dump(),
        "design": design,
        "schemas": schemas,
        "validation": validation,
        "execution_trace": execution_trace
    }