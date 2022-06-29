from transfermarkt import crawler
from transfermarkt.cellconfig import CellConfig
from transfermarkt.cellconfig import CellOperation
from transfermarkt.models import Club, Competition
from transfermarkt.utils import current_season

COMPETITIONS_ENDPOINT = "/wettbewerbe/europa/wettbewerbe"

COMPETITION_CONFIGS = {
    2: [
        CellConfig("name", CellOperation.read_link_title),
        CellConfig("id", CellOperation.read_link_href)
    ],
    3: [CellConfig("country", CellOperation.read_img_title)],
    4: [CellConfig("total_clubs", CellOperation.read_int)],
    5: [CellConfig("total_players", CellOperation.read_int)],
    6: [CellConfig("avg_age", CellOperation.read_float)],
    7: [CellConfig("foreigners_percent", CellOperation.read_percentage)],
    9: [CellConfig("total_value", CellOperation.read_string)],
}

CLUB_CONFIGS = {
    1: [
        CellConfig("name", CellOperation.read_link_title),
        CellConfig("id", CellOperation.read_link_href)
    ],
    2: [CellConfig("total_players", CellOperation.read_int)],
    3: [CellConfig("avg_age", CellOperation.read_float)],
    4: [CellConfig("total_foreigners", CellOperation.read_int)],
    5: [CellConfig("avg_market_value", CellOperation.read_string)],
    6: [CellConfig("market_value", CellOperation.read_string)],
}


def list_competitions() -> list:
    soup = crawler.fetch_content(COMPETITIONS_ENDPOINT)
    items_table = soup.find_all("table", {"class": "items"})[0]
    content = items_table.select("tbody > tr")[1:]

    return [__model_from_row(
        Competition, row, COMPETITION_CONFIGS
    ) for row in content]


def list_clubs(
        competition: Competition,
        season: int = current_season()
) -> list:
    soup = crawler.fetch_content(
        competition.id + f"/plus/?saison_id={season}"
    )
    items_table = soup.find_all("table", {"class": "items"})[0]
    content = items_table.select("tbody > tr")

    return [__model_from_row(Club, row, CLUB_CONFIGS) for row in content]


def __model_from_row(resource, row, configs_map):
    model = {}
    cells = row.select("td")

    for index, configs in configs_map.items():
        for config in configs:
            model[config.name] = config.extract(cells[index])

    return resource(**model)
