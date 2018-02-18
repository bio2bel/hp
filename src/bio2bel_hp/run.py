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


def write_belns(file):
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, encoding=MODULE_ENCODING)
    return ontology.write_namespace(file)


def deploy_to_arty():
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, encoding=MODULE_ENCODING)
    return ontology.deploy_namespace()
