from typing import Literal
from dominio.entities import Vehicle, Renting

class VehicleRepoSQL:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_vehicles(self):
        self.cursor.execute("SELECT * FROM vehicles")
        rows = self.cursor.fetchall()
        return [Vehicle(*row) for row in rows]

    def get_vehicles_by_license(self, license_plate):
        self.cursor.execute("SELECT * FROM vehicles WHERE license_plate = ?", (license_plate))
        row = self.cursor.fetchone()
        return Vehicle(*row) if row else None

    def register_vehicle(self, brand, model, license_plate, category: Literal["SUV", "Hatch", "Sedan"], daily_value):
        self.cursor.execute("INSERT INTO vehicles (brand, model, license_plate, category, daily_rent) VALUES (?, ?, ?, ?, ?)", (brand, model, license_plate, category, daily_value))
        self.connection.commit()

    def delete_vehicle(self, license_plate):
        self.cursor.execute("DELETE FROM vehicles WHERE license_plate = ?", (license_plate))
        self.connection.commit()


class RentingRepoSQL:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_vehicle_by_license_plate(self, license_plate):
        self.cursor.execute("SELECT * FROM rentings WHERE license_plate = ?", (license_plate))
        rows = self.cursor.fetchall()
        return [Renting(*row) for row in rows]

    def register_renting(self, renting_id, client_id, license_plate, start_rent_date, end_rent_date):
        self.cursor.execute("INSERT INTO rentings (renting_id, client_id, license_plate, starting_renting, ending_renting) VALUES (?, ?, ?, ?, ?)", (renting_id, client_id, license_plate, start_rent_date, end_rent_date))
        self.connection.commit()

    def delete_renting(self, renting_id):
        self.cursor.execute("DELETE FROM rentings WHERE renting_id = ?", (renting_id))
        self.connection.commit()