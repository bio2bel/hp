# -*- coding: utf-8 -*-

"""Manager for Bio2BEL HP."""

from .parser import get_obo


class Manager:
    def __init__(self):
        self.obo = get_obo()
