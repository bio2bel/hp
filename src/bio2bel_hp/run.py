# -*- coding: utf-8 -*-

from pybel.constants import NAMESPACE_DOMAIN_BIOPROCESS
from pybel_tools.ols_utils import OlsNamespaceOntology

__all__ = [
    'MODULE_NAME',
    'MODULE_DOMAIN',
    'MODULE_ENCODING',
    'write_belns',
    'deploy_to_arty',
]

MODULE_NAME = 'hp'
MODULE_DOMAIN = NAMESPACE_DOMAIN_BIOPROCESS
MODULE_ENCODING = 'BAO'

ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, encoding=MODULE_ENCODING)

write_belns = ontology.write_namespace
deploy_to_arty = ontology.deploy_namespace

if __name__ == '__main__':
    import logging
    import os

    logging.basicConfig(level=10)

    with open(os.path.expanduser('~/Desktop/hp.belns'), 'w') as f:
        ontology.write_namespace(f)
