python
import sys
import os
sys.path.insert(0, os.path.dirname(file))

from app.main import app

application = app

if name == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

