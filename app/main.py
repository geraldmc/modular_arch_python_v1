import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # add project root to sys.path

# NOTE: Run this with `python app/main.py` from the project root. 

from fastapi import FastAPI
from routers import informatic_router

app = FastAPI()

app.include_router(informatic_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", port=8000, host="127.0.0.1", reload=True)