from fastapi import HTTPException
from models.models import Asset
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
# Define a Pydantic model for the asset data
class AssetData(BaseModel):
    asset_id: str
    asset_name: str
    asset_type: str
    location: str = None
    purchase_date: datetime
    initial_cost: float
    operational_status: str = None
    
# MongoDB connection URI
MONGODB_URI = "mongodb+srv://somnathroy0340:nWXgQlhalZzcS12X@cluster0.okzjo3u.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI"

# Function to get the database and collection
async def get_database_and_collection():
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client.get_database("FastAPI")
    collection = db.get_collection("assets")
    return db, collection

# Function to create a new asset
async def create_asset(asset: Asset):
    try:
        db, collection = await get_database_and_collection()
        asset_data = asset.model_dump()
        result = await collection.insert_one(asset_data)
        return {"success": True, "message": "Asset Created Successfully"}
    except Exception as e:
        print(f"Error creating asset: {e}")
        raise HTTPException(status_code=400, detail="Failed to create asset")

# Function to get all assets
async def get_assets():
    try:
        db, collection = await get_database_and_collection()
        assets = await collection.find().to_list(length=None)
        # Create a list of AssetData objects from the assets list
        asset_data_list = [AssetData(**asset) for asset in assets]
        # Return the list of AssetData objects along with success and message
        return {"success": True, "message": "Entire asset Data is fetched", "assets": asset_data_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Function to get an asset by its ID
async def get_asset_by_id(id: str):
    try:
        db, collection = await get_database_and_collection()
        object_id = ObjectId(id)
        asset = await collection.find({"_id": object_id}).to_list(length=None)
        asset_data_list = [AssetData(**asset) for asset in asset]
        return {"success": True, "message": "Asset retrieved successfully" , "asset": asset_data_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Function to update an asset by its ID
async def update_asset(id: str, asset: Asset):
    try:
        db, collection = await get_database_and_collection()
        object_id = ObjectId(id)
        updated_asset = await collection.update_one({"_id": object_id}, {"$set": asset.model_dump()})

        if updated_asset.modified_count:
            return {"success": True, "data": {"id": id}, "message": "Asset updated successfully"}
        else:
            # If the asset was not found, raise a 404 Not Found error
            raise HTTPException(status_code=404, detail=f"Asset with id {id} not found")
    except HTTPException:
        # If an HTTPException was already raised, re-raise it
        raise
    except Exception as e:
        # If any other exception occurred, raise a 500 Internal Server Error with the error details
        raise HTTPException(status_code=500, detail=str(e))
    
# Function to delete an asset by its ID
async def delete_asset(id: str):
    try:
        db, collection = await get_database_and_collection()
        object_id = ObjectId(id)
        deleted_asset = await collection.find_one_and_delete({"_id": object_id})
        return {"success": True,"message": "Asset deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

