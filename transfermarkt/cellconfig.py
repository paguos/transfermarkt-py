from collections import namedtuple


CellConfig = namedtuple('CellConfig', ['name', 'extract'])


class CellOperation:

    @staticmethod
    def read_string(cell) -> str:
        return cell.string

    @staticmethod
    def read_float(cell) -> float:
        return float(cell.string)

    @staticmethod
    def read_int(cell) -> int:
        return int(cell.string)

    @staticmethod
    def read_percentage(cell) -> float:
        return float(cell.string.replace("%", ""))

    @staticmethod
    def read_img_title(cell) -> str:
        return cell.img["title"]

    @staticmethod
    def read_link_title(cell) -> str:
        return cell.select("a")[0]["title"]

    @staticmethod
    def read_link_href(cell) -> str:
        return cell.select("a")[0]["href"]
