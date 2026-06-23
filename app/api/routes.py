from fastapi import APIRouter
from app.schemas.request import TextRequest
from app.services.llm_service import generate_app_plan

router = APIRouter()

@router.post("/generate-app")
def generate_app(request: TextRequest):
    output = generate_app_plan(request.text)

    return {
        "input": request.text,
        "generated_plan": output
    }