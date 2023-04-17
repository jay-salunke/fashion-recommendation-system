import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from starlette.staticfiles import StaticFiles
from routers import auth, users, items,recommend
from databases.database import engine
from databases import models, crud
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["http://myproject.local:3000"]
app.middleware(
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


)
# Include Authentication Router
app.include_router(auth.router)
# Include Users Information Router
app.include_router(users.router)
# Include Items Information Router
app.include_router(items.router)
app.include_router(recommend.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
    