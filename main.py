python
from fastapi import FastAPI

Create the FastAPI app with proper title
app = FastAPI(
    title="SENTINEL OSINT Panel",
    description="Cybersecurity and geospatial intelligence platform",
    version="1.0.0"
)

Define your routes
@app.get("/")
def read_root():
    return {
        "message": "SENTINEL OSINT Panel is running",
        "status": "healthy",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/ping")
def ping():
    return {"message": "pong"}

This is the exact entrypoint Vercel needs to find
application = app

