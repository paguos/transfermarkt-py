import pytest

import transfermarkt as tm

from transfermarkt.models import Club
from transfermarkt.models import Competition


@pytest.fixture
def test_competition():
    return Competition(**{
        "name": "Premier League",
        "id": "/premier-league/startseite/wettbewerb/GB1",
        "country": "England",
        "total_clubs": 20,
        "total_players": 564,
        "avg_age": 27.1,
        "foreigners_percent": 63.1,
        "total_value": "€8.79bn"
    })


@pytest.fixture
def test_club():
    return Club(**{
        "id": "/fc-arsenal/startseite/verein/11/saison_id/2018",
        "name": "Arsenal FC",
        "total_players": 42,
        "avg_age": 24.9,
        "total_foreigners": 28,
        "avg_market_value": "€15.69m",
        "market_value": "€659.05m"
    })


@pytest.mark.vcr()
def test_list_competitions(test_competition):
    competitions = tm.list_competitions()
    expected_competitions = 25

    assert expected_competitions == len(competitions)
    assert test_competition in competitions


@pytest.mark.vcr()
def test_list_clubs(test_competition, test_club):
    clubs = tm.list_clubs(test_competition, season=2018)
    expected_clubs = 20

    assert expected_clubs == len(clubs)
    assert test_club in clubs
