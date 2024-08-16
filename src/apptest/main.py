from fastapi import FastAPI
from .api.v1.router import router
from fastapi.middleware import cors


app = FastAPI(
    title="Test FastAPI",
    description="A test project for FastAPI",
    version="0.1.0",
)

app.include_router(router, prefix="/api/v1")
app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    expose_headers=["*"],
    max_age=600,
)