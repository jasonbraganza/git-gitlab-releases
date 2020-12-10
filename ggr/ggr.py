import argparse
import re

import requests
from bs4 import BeautifulSoup

gen_err_msg = "Something’s off. Please check the url you typed in - "


def ggr():
    gru = get_url()
    parsed_raw_release = parse_gl_url(gru)
    if parsed_raw_release:
        print(parsed_raw_release)


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
    gl_rl_page_regex_pattern = re.compile(r"https://gitlab.com/.*?/.*?/-/releases")
    url_after_check = gl_rl_page_regex_pattern.search(url)
    if url_after_check:
        r = requests.get(url)
        try:
            if not r.raise_for_status():
                return r.text
            else:
                print(f"{gen_err_msg}{url}")
        except requests.exceptions.HTTPError:
            print(f"{gen_err_msg}{url}")
    else:
        print(f"{gen_err_msg}{url}")


if __name__ == "__main__":
    ggr()
