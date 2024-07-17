

from utils.common import ServiceFare,ServiceType
from utils.utils import calculate_distance

class EstimateServiceImpl:

    async def get_estimate(self, src_long: float, src_lat: float, dest_long: float, dest_lat: float) -> dict:
        estimate_fare = {}
        
        approx_distance = calculate_distance(src_long,src_lat,dest_long,dest_lat)
        
        base_fare = 10
        for service_type in ServiceType:
            try:
                fare_per_km = ServiceFare[service_type.name].value
                total_fare = base_fare + round(approx_distance * fare_per_km, 2)
                estimate_fare[service_type.name] = total_fare
            except KeyError:
                pass

        if estimate_fare:
            return estimate_fare
        
        return {"message":"Unable to provide estimates at the moment"}







