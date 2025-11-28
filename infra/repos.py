from typing import Literal

class VehicleRepo:
    def __init__(self, connection):
        self.connection = connection 
        self.cursor = self.connection.cursor()
    
    def get_vehicles(self):
        self.cursor.execute("SELECT * FROM vehicles")
        return self.cursor.fetchall()
    
    def register_vehicle(self, brand, model, license_plate, category: Literal["SUV", "Hatch", "Sedan"], daily_value):
        self.cursor.execute("INSERT INTO vehicles (brand, model, license_plate, category) VALUES (?, ?, ?, ?, ?)", (brand, model, license_plate, category, daily_value))
        self.connection.commit()

class RentingRepo:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        
    def get_vehicle_by_license_plate(self, license_plate):
        self.cursor.execute("SELECT * FROM renting WHERE license_plate = ?", (license_plate))
        return self.cursor.fetchall()
    
    def register_renting(self, renting_id, client_id, license_plate, start_rent_date, end_rent_date):
        self.cursor.execute("INSERT INTO rentings (renting_id, client_id, license_plate, start_date, end_date) VALUES (?, ?, ?, ?, ?)", (renting_id, client_id, license_plate, start_rent_date, end_rent_date))
        self.connection.commit()

    def delete_renting(self, renting_id):
        self.cursor.execute("DELETE FROM rentings WHERE renting_id = ?", (renting_id))
        self.connection.commit()