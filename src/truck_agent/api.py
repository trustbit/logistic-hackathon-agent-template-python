"""
Data types that are passed to the agents and expected in return
"""
from typing import List, Dict, Literal, Union


# World information
from pydantic import BaseModel


class Location(BaseModel):
    name: str
    roads: Dict[str, float]


class WorldInfo(BaseModel):
    locations: List[Location]
    fuel_cost: float  # euros per liter


# Current cargo information

class CargoOffer(BaseModel):
    uid: int  # unique cargo id
    origin: str
    dest: str
    name: str
    price: float  # how much do you get for the cargo
    eta_to_cargo: float
    km_to_cargo: float
    km_to_deliver: float
    eta_to_deliver: float


class TruckState(BaseModel):
    balance: float
    uid: int
    loc: str
    hours_since_full_rest: float
    time: float


class DecideRequest(BaseModel):
    truck: TruckState
    offers: List[CargoOffer]


class DecideResponse(BaseModel):
    command: Literal["DRIVE", "DELIVER", "SLEEP"]
    argument: Union[str, int, None] = None

