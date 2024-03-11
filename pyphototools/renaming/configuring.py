import argparse

from pyphototools import settings
from pyphototools.renaming import processing

parser_args = {'name': "rename", 'help': "Rename photo files",
               'description': "Renames photo files using a date template."}


def populate_argument_parser(rename_parser: argparse.ArgumentParser):
    rename_parser.add_argument("dir",
                               help="Directory containing the files", default=".")
    rename_parser.add_argument('-d', '--dateformat',
                               default=settings.date_format,
                               help="Format to use for renaming")


def parse_arguments(args):
    settings.processing_dir = args.dir
    settings.date_format = args.date_format

    return processing
