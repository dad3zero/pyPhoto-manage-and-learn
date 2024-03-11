import argparse

import pyphototools.renaming.configuring as rename_config
import pyphototools.cleaning.configuring as cleaning_config


def populate_argument_parser(global_parser: argparse.ArgumentParser):
    global_parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Every action will be displayed.')
    global_parser.add_argument('-t', '--test',
                        action='store_true',
                        help="If present, renaming will only be tested and the name sent to the output without "
                             "modifying the file. Forces -v")


def parse_arguments(args):
    pass

_actions = {}

parser = argparse.ArgumentParser(prog="pyphototools",
                                 description="Tools for photo management")
subparsers = parser.add_subparsers(dest="command", required=True)

populate_argument_parser(parser)

rename_parser = subparsers.add_parser(**rename_config.parser_args)
rename_config.populate_argument_parser(rename_parser)
_actions[rename_config.parser_args['name']] = rename_config

cleanup_parser = subparsers.add_parser(**cleaning_config.parser_args)
cleaning_config.populate_argument_parser(cleanup_parser)
_actions[cleaning_config.parser_args['name']] = cleaning_config

args = parser.parse_args()

_actions[args.command]
