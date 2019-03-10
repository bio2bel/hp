# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_hp arty`"""

from typing import Optional, TextIO

import click

from bel_resources.obo import convert_obo_graph_to_belns
from .parser import get_obo


@click.group()
def main():
    """Human Phenotype Ontology to BEL."""


@main.command()
@click.option('-f', '--file', type=click.File('w'))
@click.option('-e', '--encoding')
@click.option('-n', '--use-names', is_flag=True)
def belns(file: TextIO, encoding: Optional[str], use_names: bool):
    """Write as a BEL namespace."""
    graph = get_obo()
    convert_obo_graph_to_belns(
        graph,
        file=file,
        encoding=encoding,
        use_names=use_names,
    )


if __name__ == '__main__':
    main()
