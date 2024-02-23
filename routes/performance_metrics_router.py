from fastapi import APIRouter
from controllers.performance_metrics_controller import (
    create_performance_metrics,
    get_performance_metrics_by_id,
    get_all_performance_metrics,
    update_performance_metrics,
    delete_performance_metrics
)

performance_metrics_router  = APIRouter()

# Performance Metrics routes
performance_metrics_router.post("/create")(create_performance_metrics)
performance_metrics_router.get("/getById/{id}")(get_performance_metrics_by_id)
performance_metrics_router.get("/getAll")(get_all_performance_metrics)
performance_metrics_router.put("/update/{id}")(update_performance_metrics)
performance_metrics_router.delete("/delete/{id}")(delete_performance_metrics)

# Export the router
__all__ = ["performance_metrics_router"]