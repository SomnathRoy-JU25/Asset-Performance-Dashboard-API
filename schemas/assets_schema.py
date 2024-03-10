#  These functions are designed to serialize a list of assets into a format that can be easily consumed,
#  potentially for tasks such as data storage, transmission, or presentation.

# dict - > map { key : value }
def asset_individual_serial(asset) -> dict:
    return{
        "id": str(asset["_id"]),
        "asset_name": asset["asset_name"],
        "asset_type": asset["asset_type"],
        "location": asset["location"],
        "purchase_date": asset["purchase_date"],
        "initial_cost": asset["initial_cost"],
        "operational_status": asset["operational_status"]
    }

#  List -> Array in Cpp
def asset_list_serial(assets) -> list:
    return [asset_individual_serial(asset) for asset in assets]
