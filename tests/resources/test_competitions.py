import pytest

import transfermarkt as tm


@pytest.mark.vcr()
def test_list_competitions():
    competitions = tm.list_competitions()

    test_competition = {
        "name": "Premier League",
        "id": "/premier-league/startseite/wettbewerb/GB1",
        "country": "England",
        "total_clubs": "20",
        "total_players": "564",
        "avg_age": "27.1",
        "foreigners_percent": "63.1 %",
        "forum": None,
        "total_value": "€8.79bn"
    }

    expected_competitions = 25

    assert len(competitions) == expected_competitions
    assert test_competition in competitions
