from fastapi import APIRouter, Depends
from controllers.asset_controller import (create_asset, get_asset_by_id, get_assets, update_asset, delete_asset)

assets_router = APIRouter()

# Assets routes
assets_router.post("/create")(create_asset)
assets_router.get("/getById/{id}")(get_asset_by_id)
assets_router.get("/getAll") ( get_assets)
assets_router.put("/update/{id}") (update_asset)
assets_router.delete("/delete/{id}") (delete_asset)

# Export the router
__all__ = ["assets_router"]