from pydantic import BaseModel
from datetime import datetime


# Define a Pydantic model for the asset data
class AssetData(BaseModel):
    asset_name: str
    asset_type: str
    location: str = None
    purchase_date: datetime
    initial_cost: float
    operational_status: str = None
