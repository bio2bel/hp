# -*- coding: utf-8 -*-

"""Constants for Bio2BEL HP."""

import os

from bio2bel import get_data_dir

MODULE_NAME = 'hp'
DATA_DIR = get_data_dir(MODULE_NAME)

OBO_URL = 'http://purl.obolibrary.org/obo/hp.obo'
OBO_PATH = os.path.join(DATA_DIR, 'hp.obo')
OBO_PREPARSED_PATH = os.path.join(DATA_DIR, 'hp.obo.gpickle')
