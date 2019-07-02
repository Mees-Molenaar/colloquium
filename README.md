# Colloquium: Investigating sirtuins using novel computational techniques

This is a project for my master study LST. 

> Europe PMC searchPublications and getAnnotations for Proteins V3.knwf

This is the knime workflow I use to obtain all the proteins. This list contains the article ID, the uniprot link to the protein and the abbreviated name.

> proteins_22-6-19.csv

This is a list made with the knime workflow and used for the python file that makes an edge list.

> make_edge_list.py

This is a python script that makes an edge-list of the protein list obtained by the knime workflow.
Probably, this is not the best written script and there is option for optimization. But it works.
This script now also includes the thresholds!

> edge_list20190701.csv

This is the csv file containing the edge list. And this file is used to make a network via cytoscape.

> introduction.docx

Currently, this document contains ideas of the contents of the introduction that I want to work out.
