python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SENTINEL OSINT Panel is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/ping")
def ping():
    return {"message": "pong"}
