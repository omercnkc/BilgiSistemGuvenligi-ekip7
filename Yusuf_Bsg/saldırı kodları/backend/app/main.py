from fastapi import FastAPI
from backend.app.api.routes_vulnerable import router

app = FastAPI()
app.include_router(router)
