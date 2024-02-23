from fastapi import APIRouter, Depends
from Insights.get_insights import get_insights
from middleware.authenticate import authenticate

insights_router = APIRouter()

# Insights route
insights_router.get("/getInsights", dependencies=[Depends(authenticate)], tags=["insights"])(get_insights)

# Export the router
__all__ = ["insights_router"]