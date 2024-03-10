from fastapi import FastAPI # Import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import CORS
# import Routes and Functions
from routes.assets_router import assets_router
from routes.performance_metrics_router import performance_metrics_router
from middleware.auth import auth

app = FastAPI()  # Initialize FastAPI

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Setting the Routes
app.include_router(auth)
app.include_router(assets_router, prefix="/api/assets", tags=["Assets"])
app.include_router(performance_metrics_router, prefix="/api/performance", tags=["Performance Matrix"])
