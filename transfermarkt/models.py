from dataclasses import dataclass


@dataclass
class Club:
    name: str
    id: str
    total_players: int
    avg_age: float
    total_foreigners: int
    avg_market_value: str
    market_value: str


@dataclass
class Competition:
    name: str
    id: str
    country: str
    total_clubs: int
    total_players: int
    avg_age: float
    foreigners_percent: float
    total_value: str
