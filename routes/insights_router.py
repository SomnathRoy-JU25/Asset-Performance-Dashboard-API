from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI =  "mongodb+srv://somnathroy0340:nWXgQlhalZzcS12X@cluster0.okzjo3u.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI"

# Function to get the MongoDB database and collection
async def get_database_and_collection():
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client.get_database("FastAPI")
    collection = db.get_collection("performancemetrics")
    return db, collection

# Function to calculate average downtime
async def calculate_average_downtime():
    try:
        db, collection = await get_database_and_collection()
        pipeline = [
            {"$group": {"_id": None, "averageDowntime": {"$avg": "$downtime"}}}
        ]
        cursor = collection.aggregate(pipeline)
        documents = await cursor.to_list(None)
        average_downtime = documents[0]["averageDowntime"] if documents else 0
        return average_downtime
    except Exception as e:
        error_message = f"Error calculating average downtime: {e}"
        print(error_message)
        raise HTTPException(status_code=500, detail=error_message)

# Function to calculate total maintenance costs
async def calculate_total_maintenance_costs():
    try:
        db, collection = await get_database_and_collection()
        pipeline = [
            {"$group": {"_id": None, "totalMaintenanceCosts": {"$sum": "$maintenance_costs"}}}
        ]
        cursor = collection.aggregate(pipeline)
        async for document in cursor:
            total_maintenance_costs = document["totalMaintenanceCosts"]
            return total_maintenance_costs
        return 0  # Return 0 if no documents are found
    except Exception as e:
        error_message = f"Error calculating total maintenance costs: {e}"
        print(error_message)
        raise HTTPException(status_code=500, detail=error_message)

# Function to identify assets with high failure rates
async def identify_assets_with_high_failure_rates():
    try:
        db, collection = await get_database_and_collection()
        threshold = 0.1  # Define threshold for high failure rate
        pipeline = [
            {"$group": {"_id": "$asset_id", "averageFailureRate": {"$avg": "$failure_rate"}}},
            {"$match": {"averageFailureRate": {"$gt": threshold}}}
        ]
        cursor = collection.aggregate(pipeline)
        documents = []
        async for document in cursor:
            documents.append(document)
        return documents
    except Exception as e:
        error_message = f"Error identifying assets with high failure rates: {e}"
        print(error_message)
        raise HTTPException(status_code=500, detail=error_message)