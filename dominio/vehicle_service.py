from dominio.entities import Vehicle

class VehicleService:
    def __init__(self, vehicle_repo):
        self.vehicle_repo = vehicle_repo

    def create_vehicle(self, brand, model, license_plate, category, daily_rent):
        vehicle_exists = self.vehicle_repo.get_vehicles_by_license(license_plate)

        if vehicle_exists:
            raise ValueError("Veículo já cadastrado!")

        self.vehicle_repo.register_vehicle(brand, model, license_plate, category, daily_rent)