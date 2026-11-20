from fastapi import FastAPI

from core.settings import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

@app.get("/api/health")
async def health():
    return {"status": "ok"}