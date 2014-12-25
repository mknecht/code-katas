import argparse
import pprint
import re
import sys

import requests


SYMBOL, INDEX = range(2)


def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("query")
    return parser.parse_args()


def get_data(url):
    return requests.get(
        url,
        headers={"accept": "application/json"},
    ).json()


def parse_query(raw_query):
    pattern = re.compile(r"(\w+)(?:\[(\d+)\])?")
    parts = []
    for dotpart in raw_query.split("."):
        match = pattern.match(dotpart)
        symbol_token, index_token = tuple(match.groups())
        parts.append((SYMBOL, symbol_token))
        if index_token:
            parts.append((INDEX, int(index_token)))
    return parts


def evaluate(query, data):
    result = data
    for tokentype, token in query:
        if tokentype in {INDEX, SYMBOL}:
            result = result[token]
    return result


def prettyprint(result):
    pprint.pprint(result)


def main(args):
    prettyprint(evaluate(parse_query(args.query), get_data(args.url)))
    return 0


if __name__ == '__main__':
    sys.exit(main(getargs()))
