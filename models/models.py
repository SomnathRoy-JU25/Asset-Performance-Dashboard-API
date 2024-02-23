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


class PerformanceMetrics(BaseModel):
    asset_id: str
    uptime: float
    downtime: float
    maintenance_costs: float
    failure_rate: float
    efficiency: float