from argparse import ArgumentParser


def read_args():
    parser = ArgumentParser()
    parser.add_argument("-p", "--partition", default="2009-01-01", help="partition of format yyyy-MM-dd")
    return parser.parse_args()
