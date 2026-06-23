from fastapi import FastAPI
from app.core.config import APP_NAME, VERSION
from app.api.routes import router

app = FastAPI(
    title=APP_NAME,
    version=VERSION
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "AppCompiler AI running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}