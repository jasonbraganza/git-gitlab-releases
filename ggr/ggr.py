import argparse
import re

import requests


def ggr():
    gru = get_url().strip()
    parse_gl_url(gru)


def get_url():
    """
    Gets and returns a url from the prompt
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url",
        type=str,
        metavar="https://gitlab.com/{some-repo}/{some-project}/-/releases",
        help="Please give a link to a complete Gitlab releases url",
    )
    args = parser.parse_args()
    return args.url


def parse_gl_url(url):

    r = requests.get(url)
    try:
        if not r.raise_for_status():
            print(r.text)
        else:
            print(f"Something’s off. Please check the url, {url}")
    except requests.exceptions.HTTPError:
        print(f"Something’s off. Please check the url you typed in - {url}")


if __name__ == "__main__":
    ggr()
