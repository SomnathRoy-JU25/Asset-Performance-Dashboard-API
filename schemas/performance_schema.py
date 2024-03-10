def performace_individual_serial(performance_matric) -> dict:
    return{
        "id": str(performance_matric["_id"]),
        "asset_name": (performance_matric["asset_name"]),
        "uptime": performance_matric["uptime"],
        "downtime": performance_matric["downtime"],
        "maintenance_costs": performance_matric["maintenance_costs"],
        "failure_rate": performance_matric["failure_rate"],
        "initial_cost": performance_matric["efficiency"],
    }


def performance_list_serial(performance_matrics) -> list:
    return [performace_individual_serial(performance_matric) for performance_matric in performance_matrics]
