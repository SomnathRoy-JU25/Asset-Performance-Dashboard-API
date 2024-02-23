from fastapi import FastAPI # Import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import CORS
from config.database import db  # Import db object from config/database.py

# Import routers
from routes.performance_metrics_router import performance_metrics_router
from routes.assets_router import assets_router
from routes.insights_router import insights_router

app = FastAPI()  # Initialize FastAPI
db = db  # Initialize db object

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(assets_router, prefix="/asset", tags=["assets"])
app.include_router(performance_metrics_router, prefix="/performance-metrics", tags=["performance metrics"])
app.include_router(insights_router, prefix="/insights", tags=["insights"])

# Testing route
@app.get("/")
async def read_root():
    return {"success": True, "message": "Your server is up and running ..."}
