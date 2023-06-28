from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass
class DatePartition:
    column: str
    value: str

    def year(self) -> str:
        return self.value[:4]

    def __repr__(self):
        return f"dt={self.value}"


def read_args():
    parser = ArgumentParser()
    parser.add_argument("-p", "--partition", default="2009-01-01", help="partition of format yyyy-MM-dd")
    return parser.parse_args()
