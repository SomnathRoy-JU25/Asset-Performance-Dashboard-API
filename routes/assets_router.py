from fastapi import APIRouter
from fastapi import HTTPException
from models.asset_model import AssetData
from config.database import collection_name1
from schemas.assets_schema import asset_list_serial
from bson import ObjectId

assets_router = APIRouter()

# Function to create a new asset
@assets_router.post("/create")
async def create_asset(asset: AssetData):
    try:
         collection_name1.insert_one(dict(asset))
         return asset
    except Exception as e:
        print(f"Error creating asset: {e}")
        raise HTTPException(status_code=400, detail="Failed to create asset")


# Function to get all assets
@assets_router.get("/getAll")
async def get_assets():
    try:
        assets = asset_list_serial(collection_name1.find())
        return assets
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Function to get an asset by its ID
@assets_router.get("/getByid/{id}")
async def get_asset_by_id(id: str):
    try:
        asset = collection_name1.find_one({"_id": ObjectId(id)})
        # Ensure asset is not None before processing
        if asset:
            # Pass the asset as a single-element list to list_serial function
            serialized_asset = asset_list_serial([asset])
            return serialized_asset[0]  # Return the first (and only) element of the list
        else:
            # Handle case where no asset is found for the given id
            raise HTTPException(status_code=404, detail="Asset not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Function to update an asset by its ID
@assets_router.put("/update/{id}")
async def update_asset(id: str, asset: AssetData):
    try:
         collection_name1.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(asset)})
         return asset
    except Exception as e:
        # If any other exception occurred, raise a 500 Internal Server Error with the error details
        raise HTTPException(status_code=500, detail=str(e))
    
    
# Function to delete an asset by its ID
@assets_router.delete("/delete/{id}")
async def delete_asset(id: str):
    try:
        collection_name1.find_one_and_delete({"_id": ObjectId(id)})
        return {"success": True, "message": "Asset deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))