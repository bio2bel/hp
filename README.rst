Human Phenotype Ontology to BEL
===============================
This repository converts the Human Phenotype Ontology (HP, [1]_) to a BEL Namespace file by using the EBI Ontology
Lookup Service.

Abstract
--------
An ontology is a computational representation of a domain of knowledge based upon a controlled, standardized
vocabulary for describing entities and the semantic relationships between them.

HP aims to provide a standardized vocabulary of phenotypic abnormalities encountered in human disease. Each term in
the HP ontology describes a phenotypic abnormality, such as atrial septal defect. The HPO is currently being developed
using the medical literature, Orphanet, DECIPHER, and OMIM. HPO currently contains approximately 11,000 terms
(still growing) and over 115,000 annotations to hereditary diseases. The HPO also provides a large set of HPO
annotations to approximately 4000 common diseases.

Installation
------------
Install directly from GitHub with:

.. code-block:: sh

   $ pip install git+https://github.com/bio2bel/hp.git

Links
-----
- `HP Official Site <http://human-phenotype-ontology.github.io>`_
- Entry in the EBI `Ontology Lookup Service <http://www.ebi.ac.uk/ols/ontologies/hp>`_

References
----------
.. [1] Köhler, *et al*. (2017) `The Human Phenotype Ontology in 2017 <http://nar.oxfordjournals.org/content/45/D1/D865>`_
       Nucl. Acids Res.
