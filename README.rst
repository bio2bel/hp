Human Phenotype Ontology to BEL
===============================
This repository converts the Human Phenotype Ontology (HP) to a BEL Namespace file by using the EBI Ontology Lookup
Service.

Citation
--------
Sebastian Köhler, Nicole Vasilevsky, Mark Engelstad, Erin Foster, et al. `The Human Phenotype Ontology in 2017 <http://nar.oxfordjournals.org/content/45/D1/D865>`_
Nucl. Acids Res. (2017) doi: 10.1093/nar/gkw1039

Abstract
--------
An ontology is a computational representation of a domain of knowledge based upon a controlled, standardized vocabulary for describing entities and the semantic relationships between them.

The Human Phenotype Ontology (HPO) aims to provide a standardized vocabulary of phenotypic abnormalities encountered in human disease. Each term in the HPO describes a phenotypic abnormality, such as atrial septal defect. The HPO is currently being developed using the medical literature, Orphanet, DECIPHER, and OMIM. HPO currently contains approximately 11,000 terms (still growing) and over 115,000 annotations to hereditary diseases. The HPO also provides a large set of HPO annotations to approximately 4000 common diseases.

Installation
------------
Install directly from GitHub with:

.. code-block:: sh

  python3 -m pip install git+https://github.com/bio2bel/hp.git

Links
-----
- `HP Official Site <http://human-phenotype-ontology.github.io>`_
- Entry in the EBI `Ontology Lookup Service <http://www.ebi.ac.uk/ols/ontologies/hp>`_
