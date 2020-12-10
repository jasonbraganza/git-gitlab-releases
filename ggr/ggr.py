import argparse
import requests


def ggr():
    get_url()


def get_url():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url",
        type=str,
        metavar="https://gitlab.com/{repo}/{project}/-/releases",
        help="Please type or paste in a link to a complete Gitlab releases url",
    )
    args = parser.parse_args()
    print(type(args.url))


if __name__ == "__main__":
    ggr()
