import sys
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


def read_args(argv: list[str] = None):
    if argv is None:
        argv = sys.argv[1:]

    parser = ArgumentParser()
    parser.add_argument("-p", "--partition", required=True, help="partition of format yyyy-MM-dd")
    return parser.parse_args(argv)
