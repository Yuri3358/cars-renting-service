class RentingFacade:
    def __init__(self, vehicle_repo, renting_repo, vehicle_service, renting_service):
        self.vehicle_repo = vehicle_repo
        self.renting_repo = renting_repo
        self.vehicle_service = vehicle_service
        self.renting_service = renting_service

    def create_vehicle(self, brand, model, license_plate, category, daily_rent):
        self.vehicle_service.create_vehicle(brand, model, license_plate, category, daily_rent)

    def get_vehicles(self):
        return self.vehicle_repo.get_vehicles()

    def get_vehicle_by_license(self, license_plate):
        return self.vehicle_repo.get_vehicles_by_license(license_plate)
    
    def create_rentings(self, renting_id, license_plate, client_id, start, end):
        return self.renting_service.create_rentings(renting_id, license_plate, client_id, start, end)
    
    def get_rentings_by_license(self, license_plate):
        return self.renting_repo.get_vehicle_by_license_plate(license_plate)