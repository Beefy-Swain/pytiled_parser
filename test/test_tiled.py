import pprint
import pickle

from io import StringIO

import pytiled_parser


pp = pprint.PrettyPrinter(indent=4, compact=True, width=100)

pp = pp.pprint

MAP_NAME = '/home/ben/Projects/pytiled_parser/pytiled_parser-venv/pytiled_parser/tests/test_data/test_map_simple.tmx'

map = pytiled_parser.parse_tile_map(MAP_NAME)

pp(map.__dict__)