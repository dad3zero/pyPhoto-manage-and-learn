import argparse

from pyphototools import settings

parser_args = {'name': 'clean_rawjpg',
               'help': 'Remove jpgs if RAW file exists.'}


def populate_argument_parser(rename_parser: argparse.ArgumentParser):
    pass


def parse_arguments(args):
    return