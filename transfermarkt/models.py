from dataclasses import dataclass

############################
# Response Classes
############################


@dataclass
class Club:
    id: int
    name: str
    total_players: int
    avg_age: float
    total_foreigners: int
    avg_market_value: str
    market_value: str


@dataclass
class Competition:
    id: str
    name: str
    country: str
    total_clubs: int
    total_players: int
    avg_age: float
    foreigners_percent: float
    total_value: str
