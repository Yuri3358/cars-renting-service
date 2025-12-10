class RentingService:
    def __init__(self, renting_repo, vehicle_repo):
        self.renting_repo = renting_repo
        self.vehicle_repo = vehicle_repo
        
    def create_renting(self, renting):
        vehicle_existence = self.vehicle_repo.get_vehicle_by_license_plate(renting.license_plate)

        if not vehicle_existence:
            raise ValueError("Veículo não encontrado!")