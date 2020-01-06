import argparse


def get_keyword():
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', help='your youtube videos keyword')
    args = parser.parse_args()

    return args.keyword
