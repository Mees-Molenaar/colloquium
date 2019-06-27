# Colloquium: Investigating sirtuins using novel computational techniques

This is a project for my master study LST. 

> Europe PMC searchPublications and getAnnotations for Proteins V3.knwf

This is the knime workflow I use to obtain all the proteins. This list contains the article ID, the uniprot link to the protein and the abbreviated name.
*I haven't been able to include thresholds yet.* 

> proteins_22-6-19.csv

This is a list made with the knime workflow and used for the python file that makes an edge list.

> make_edge_list.py

This is a python script that makes an edge-list of the protein list obtained by the knime workflow.
Probably, this is not the best written script and there is option for optimization. But it works.
*I didn't include the edge_list.csv, since it is quite big.*
