from transfermarkt import crawler
from transfermarkt.models import Club, Competition
from transfermarkt.utils import current_season, DataCell

############################
# Configurations
############################

COMPETITIONS_ENDPOINT = "/wettbewerbe/europa/wettbewerbe"

CLUB_ENDPOINT = "/competitions/startseite/wettbewerb"

############################
# Functions
############################


def list_competitions() -> list:
    soup = crawler.fetch_content(COMPETITIONS_ENDPOINT)
    items_table = soup.find_all("table", {"class": "items"})[0]
    content = items_table.select("tbody > tr")[1:]

    return [Competition(
        **parse_competition(row.select("td"))
    ) for row in content]


def list_clubs(
        competition: Competition,
        season: int = current_season()
) -> list:
    soup = crawler.fetch_content(
        f"{CLUB_ENDPOINT}/{competition.id}/plus/?saison_id={season}"
    )
    items_table = soup.find_all("table", {"class": "items"})[0]
    content = items_table.select("tbody > tr")

    return [Club(
        **parse_club(row.select("td"))
    ) for row in content]


############################
# Helpers
############################


def parse_competition(table_row):
    return {
        "id": DataCell(table_row[2]).link_href().extract_competition_id().read(),
        "name": DataCell(table_row[2]).link_title().read(),
        "country": DataCell(table_row[3]).img_title().read(),
        "total_clubs": DataCell(table_row[4]).to_int().read(),
        "total_players": DataCell(table_row[5]).to_int().read(),
        "avg_age": DataCell(table_row[6]).to_float().read(),
        "foreigners_percent":
        DataCell(table_row[7]).to_string().parse_percentage().read(),
        "total_value": DataCell(table_row[9]).to_string().read(),
    }


def parse_club(table_row):
    return {
        "id": DataCell(table_row[1]).link_href().extract_club_id().read(),
        "name": DataCell(table_row[1]).link_title().read(),
        "total_players": DataCell(table_row[2]).to_int().read(),
        "avg_age": DataCell(table_row[3]).to_float().read(),
        "total_foreigners": DataCell(table_row[4]).to_int().read(),
        "avg_market_value": DataCell(table_row[5]).to_string().read(),
        "market_value": DataCell(table_row[6]).to_string().read(),
    }
