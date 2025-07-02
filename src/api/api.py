from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import user_router

app = FastAPI(title="FastAPI Example",
    description="A simple FastAPI application example",
    summary="FastAPI Example API",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",  # React app running on localhost
    "http://localhost:5173",  # Vite development server
    "http://localhost:4173",  # Vite development server alternative port
    "localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["POST", "PUT", "GET", "DELETE", "PATCH"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(user_router)

@app.get("/")
async def root():
    return {"detail": "Welcome to the FastAPI Example!"}