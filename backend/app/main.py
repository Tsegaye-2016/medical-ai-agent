from fastapi import FastAPI
from app.routes.ai import router
from app.routes import debug, summary
app = FastAPI()

app.include_router(router, prefix="/ai")

app.include_router(debug.router)
app.include_router(summary.router)