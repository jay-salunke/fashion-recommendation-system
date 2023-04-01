from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.routers import auth, users, items
from app.databases.database import engine
from app.databases import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include Authentication Router
app.include_router(auth.router)
# Include Users Information Router
app.include_router(users.router)
# Include Items Information Router
app.include_router(items.router)
# Serving the Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
