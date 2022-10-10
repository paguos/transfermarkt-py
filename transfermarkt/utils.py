import re

from datetime import date


def current_season() -> int:
    return __get_season(date.today())


def __get_season(input_date: date) -> int:
    end_season = date(day=30, month=6, year=input_date.year)
    delta = input_date - end_season

    if delta.days > 0:
        return input_date.year
    else:
        return input_date.year - 1


class DataCell:

    def __init__(self, value) -> None:
        self.value = value

    def read(self):
        return self.value

    ############################
    # Basic operations
    ############################

    def to_string(self):
        self.value = self.value.string
        return self

    def to_float(self):
        self.value = float(self.value.string)
        return self

    def to_int(self):
        self.value = int(self.value.string)
        return self

    ############################
    # Tag Operations
    ############################

    def img_title(self):
        self.value = self.value.img["title"]
        return self

    def link_href(self):
        self.value = self.value.select("a")[0]["href"]
        return self

    def link_title(self):
        self.value = self.value.select("a")[0]["title"]
        return self

    ############################
    # Parsing operations
    ############################

    def parse_percentage(self):
        self.value = float(self.value.replace("%", ""))
        return self

    def extract_competition_id(self):
        match = re.match(r"/(.*)/startseite/wettbewerb/(.*)", self.value)

        if match:
            self.value = match.group(2)
            return self

    def extract_club_id(self):
        match = re.match(r"/(.*)/startseite/verein/(\d+)/(.*)", self.value)

        if match:
            self.value = int(match.group(2))
            return self
