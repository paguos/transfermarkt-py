from transfermarkt.core import crawler
from transfermarkt.core import GenericStruct

COMPETITIONS_ENDPOINT = "/wettbewerbe/europa/wettbewerbe"

COMPETITION_FIELDS = ["competition", "country", "total_clubs", "total_players",
                      "avg_age", "foreigners_percent", "forum", "total_value"]

CLUB_FIELDS = ["total_players", "avg_age",
               "total_foreigners", "avg_market_value", "market_value"]


def list_competitions() -> list:
    soup = crawler.fetch_content(COMPETITIONS_ENDPOINT)
    items_table = soup.find_all("table", {"class": "items"})[0]
    content = items_table.select("tbody > tr")[1:]

    return [__row_to_competition(row, COMPETITION_FIELDS) for row in content]


def list_clubs(competition) -> list:
    soup = crawler.fetch_content(competition.id)
    items_table = soup.find_all("table", {"class": "items"})[0]
    content = items_table.select("tbody > tr")

    return [__row_to_club(row, CLUB_FIELDS) for row in content]


def __row_to_competition(row, headers: list) -> GenericStruct:
    competition = {}
    cells = row.select("td")

    for index in range(0, len(cells)):
        cell = cells[index]

        if index == 2:
            link = cell.select("a")[0]
            competition["name"] = link["title"]
            competition["id"] = link["href"]
        elif index == 3:
            competition[headers[index - 2]] = cell.img["title"]
        elif index >= 4:
            competition[headers[index-2]] = cell.string

    return GenericStruct(**competition)


def __row_to_club(row, headers: list) -> GenericStruct:
    club = {}
    cells = row.select("td")

    for index in range(0, len(cells)):
        cell = cells[index]

        if index == 1:
            link = cell.select("a")[0]
            club["name"] = link["title"]
            club["id"] = link["href"]
        elif index >= 2:
            club[headers[index-2]] = cell.string

    return GenericStruct(**club)
