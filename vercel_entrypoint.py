python
from fastapi import FastAPI

Create the app
app = FastAPI(title="SENTINEL OSINT Panel")

@app.get("/")
def read_root():
    return {"message": "SENTINEL OSINT Panel is running", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/ping")
def ping():
    return {"message": "pong"}

For Vercel - this is the required entrypoint
def main():
    return app

This is what Vercel expects as the handler
application = app

