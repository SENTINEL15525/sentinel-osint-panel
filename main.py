python
from fastapi import FastAPI

Create the FastAPI app
app = FastAPI()

Define routes
@app.get("/")
def read_root():
    return {"message": "SENTINEL OSINT Panel is running", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/ping")
def ping():
    return {"message": "pong"}

For Vercel - this is the exact entrypoint Vercel looks for
def main():
    return app

Alternative entrypoint that Vercel might prefer
application = app

