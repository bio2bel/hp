# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_hp arty`"""

from __future__ import print_function

import logging

import click

from .run import deploy_to_arty


@click.group()
def main():
    """Human Phenotype Ontology to BEL"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
@click.option('-b', '--ols-base', help="Custom OLS base url")
def deploy(ols_base=None):
    """Deploy BEL namespace to Artifactory"""
    success = deploy_to_arty(ols_base=ols_base)
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


if __name__ == '__main__':
    main()
