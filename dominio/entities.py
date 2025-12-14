from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class Vehicle:
    brand: str
    model: str
    license_plate: str
    category: Literal["SUV", "Sedan", "Hatch"]
    daily_rent: float

@dataclass
class Renting:
    renting_id: str
    license_plate: str
    client_id: str
    start: date
    end: date