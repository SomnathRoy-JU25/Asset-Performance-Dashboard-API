from fastapi import APIRouter, HTTPException
from models.performance_matrics_model import PerformanceMetrics
from config.database import collection_name2
from schemas.performance_schema import performance_list_serial
from bson import ObjectId

performance_metrics_router = APIRouter()

# Function to create a new performance metrics
@performance_metrics_router.post("/create")
async def create_performance_metrics(performance_metrics: PerformanceMetrics):
    try:
        collection_name2.insert_one(dict(performance_metrics))
        return performance_metrics, {"success": True, "message": "Performance Metrics Created Successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to create performance metrics")


# Function to get a performance metrics by ID
@performance_metrics_router.get("/getById/{id}")
async def get_performance_metrics_by_id(id: str):
    try:
        performance_metrics = collection_name2.find_one({"_id": ObjectId(id)})
        # Ensure asset is not None before processing
        if performance_metrics:
            # Pass the asset as a single-element list to list_serial function
            serialized_asset = performance_list_serial([performance_metrics])
            return serialized_asset[0]  # Return the first (and only) element of the list
        else:
            # Handle case where no asset is found for the given id
            raise HTTPException(status_code=404, detail="performance_metrics not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Function to get all performance metrics
@performance_metrics_router.get("/getAll")
async def get_all_performance_metrics():
    try:
        performance_metrics = performance_list_serial(collection_name2.find())
        return performance_metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Function to update a performance metrics
@performance_metrics_router.put("/update/{id}")
async def update_performance_metrics(id: str, performance_metrics: PerformanceMetrics):
    try:
        collection_name2.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(performance_metrics)})
        return performance_metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Function to delete a performance metrics
@performance_metrics_router.delete("/delete/{id}")
async def delete_performance_metrics(id: str):
    try:
        collection_name2.find_one_and_delete({"_id": ObjectId(id)})
        return {"success": True, "message": "Performance Metrics deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

