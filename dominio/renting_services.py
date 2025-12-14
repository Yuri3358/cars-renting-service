from dominio.entities import Renting
from dominio.regras import RentingRules
from datetime import date

class RentingService:
    def __init__(self, renting_repo, vehicle_repo):
        self.renting_repo = renting_repo
        self.vehicle_repo = vehicle_repo

    def create_renting(self, renting_id: str, license_plate: str, client_id: str, start: date, end: date):
        vehicle_existence = self.vehicle_repo.get_vehicles_by_license(license_plate)

        if not vehicle_existence:
            raise ValueError("Veículo não encontrado!")

        renting = Renting(renting_id, license_plate, client_id, start, end)

        current_rentings = self.renting_repo.get_vehicle_by_license_plate(license_plate)

        RentingRules.check_renting_conflicts(renting, current_rentings)

        RentingRules.check_renting_period(renting, min_days=1, max_days=30)

        renting_price = RentingRules.renting_price_calc(renting, vehicle_existence)

        self.renting_repo.register_renting(renting_id, license_plate, client_id, start, end)

        return renting_price
