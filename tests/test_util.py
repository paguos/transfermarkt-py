from freezegun import freeze_time

from transfermarkt.utils import current_season


def test_current_season():
    # Test day in the second half of the season
    with freeze_time("2015-03-20"):
        assert 2014 == current_season()

    # Test day in the first half of the season
    with freeze_time("2015-09-20"):
        assert 2015 == current_season()
