from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class Veiculo:
    id: str
    placa: str
    categoria: Literal["SUV", "Sedan", "Hatch"]
    valor_diaria: float

@dataclass
class Locação:
    id_locacao: str
    id_veiculo: str
    cliente: str
    inicio: date
    termino: date