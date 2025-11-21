from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class Vehicle:
    brand: str
    model: str
    license_plate: str
    categy: Literal["SUV", "Sedan", "Hatch"]
    daily_rent: float

@dataclass
class Renting:
    renting_id: str
    license_plae: str
    client_id: str
    starting: date
    ending: date