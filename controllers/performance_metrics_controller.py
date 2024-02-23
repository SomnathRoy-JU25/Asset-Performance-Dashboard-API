from fastapi import HTTPException
from models.models import PerformanceMetrics
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime

class Asset(BaseModel):
    asset_id: str
    asset_name: str
    asset_type: str
    location: str = None
    purchase_date: datetime
    initial_cost: float
    operational_status: str = None

# Assuming you have defined your MongoDB connection URI
MONGODB_URI = "mongodb+srv://somnathroy0340:nWXgQlhalZzcS12X@cluster0.okzjo3u.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI"

# Define a function to get the MongoDB database and collection
async def get_database_and_collection():
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client.get_database("FastAPI")
    collection = db.get_collection("performancemetrics")
    return db, collection

# Define a function to create a new performance metrics
async def create_performance_metrics(performance_metrics: PerformanceMetrics):
    try:
        db, collection = await get_database_and_collection()
        performance_metrics_data = performance_metrics.model_dump()
        result = await collection.insert_one(performance_metrics_data)
        return {"success": True, "message": "Performance Metrics Created Successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to create performance metrics")

# Define a function to get a performance metrics by ID
async def get_performance_metrics_by_id(id: str):
    try:
        _, collection = await get_database_and_collection()
        object_id = ObjectId(id)
        performance_metrics = await collection.find({"_id": object_id}).to_list(length=None)
        formatted_performance_metrics_list = [{**item, "_id": str(item["_id"])} for item in performance_metrics]
        return {"success": True,"data": formatted_performance_metrics_list,
                "message": "Performance Metrics retrieved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define a function to get all performance metrics
async def get_all_performance_metrics():
    try:
        db, collection = await get_database_and_collection()
        # Retrieve all performance metrics documents
        performance_metrics_list = await collection.find().to_list(length=None)
        formatted_performance_metrics_list = [{**item, "_id": str(item["_id"])} for item in performance_metrics_list]
        return {"success": True, "data": formatted_performance_metrics_list, "message": "All Performance Metrics retrieved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define a function to update a performance metrics
async def update_performance_metrics(id: str, performance_metrics: PerformanceMetrics):
    try:
        # Get the MongoDB collection
        _, collection = await get_database_and_collection()
        object_id = ObjectId(id)
        updated_performance_metrics = await collection.update_one({"_id": object_id}, 
                                                                {"$set": performance_metrics.model_dump()})
    
        if updated_performance_metrics.modified_count:
            return {"success": True, "data": {"id": id}, "message": "Performance Metrics Updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Performance Metrics not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define a function to delete a performance metrics
async def delete_performance_metrics(id: str):
    try:
        db, collection = await get_database_and_collection()
        object_id = ObjectId(id)
        deleted_performance_metrics = await collection.find_one_and_delete({"_id": object_id})
        return {"success": True,"message": "Performance Matrics deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e) )

