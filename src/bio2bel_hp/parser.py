# -*- coding: utf-8 -*-

"""Parsers for Bio2BEL HP."""

from bio2bel.obo import make_obo_getter
from .constants import OBO_PATH, OBO_PREPARSED_PATH, OBO_URL

__all__ = [
    'get_obo',
]

get_obo = make_obo_getter(OBO_URL, OBO_PATH, preparsed_path=OBO_PREPARSED_PATH)
