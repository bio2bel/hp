# -*- coding: utf-8 -*-

from pybel.constants import NAMESPACE_DOMAIN_BIOPROCESS
from pybel_tools.definition_utils import write_namespace
from pybel_tools.resources import deploy_namespace, get_today_arty_namespace

from ols_client import get_labels

__all__ = [
    'MODULE_NAME',
    'deploy_to_arty'
]

MODULE_NAME = 'human-phenotype-ontology'


def write_belns(file, ols_base=None):
    values = get_labels('hp', ols_base=ols_base)
    write_namespace(
        namespace_name='Human Phenotype Ontology',
        namespace_keyword='HP',
        namespace_domain=NAMESPACE_DOMAIN_BIOPROCESS,
        author_name='Charles Tapley Hoyt',
        author_contact='charles.hoyt@scai.fraunhofer.de',
        author_copyright='Creative Commons by 4.0',
        citation_name='Human Phenotype Ontology',
        values=values,
        functions='O',
        file=file
    )


def deploy_to_arty(ols_base=None):
    """Gets the data and writes BEL namespace file to artifactory

    :return: The resource path, if it was deployed successfully, else none.
    :rtype: str
    """

    file_name = get_today_arty_namespace(MODULE_NAME)

    with open(file_name, 'w') as file:
        write_belns(file, ols_base=ols_base)

    return deploy_namespace(file_name, MODULE_NAME)
