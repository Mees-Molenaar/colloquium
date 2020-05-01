# Colloquium: Investigating Sirtuins in Alzheimer's Disease using novel computational techniques

This project consists of my colloquim for the Master Life Science and Technology at Leiden University.

### Abstract
The most prevalent neurodegenerative disease is Alzheimer’s Disease (AD). No breakthrough
treatment has been found yet, indicating the importance of researching this disease further.
However, an enormous amount of research is performed each year (15,018 articles in 2018 alone),
which makes it impossible for humans to analyse and group all the gathered information. Therefore,
tools should be developed to summarize this vast amount of information. In this work, we used a
novel and reusable text-mining based approach to investigate recent protein interactions with SIRT1
relating to AD. A protein network was created consisting of co-occurrences and three novel proteins
interacting with SIRT1 were found. SIRT1 is upregulated by FOXQ1, which prevents apoptosis. SIRT1
is also upregulated by S1PR1, however, there are also contradictory findings. Lastly, CLDN5, which is
important in the integrity of the blood-brain barrier (BBB), is regulated by SIRT1. These discoveries
show that using this text-mining approach we were able to find recent interactions of SIRT1 in AD.

### File List

> protein_list_20200217.csv

This csv file contains the protein list that was retreived using the Jupyter Notebook. Unfortunately, the created edge-list was to large to upload to Github. However, you can easely use this list of proteins to create the edge-list yourself.

> europepmc_edge_list.ipynb

This is the Jupyter Notebook that was used to retrieve the proteins from the EuropePMC database. Additionally, with this protein list the edge-list was created.

The Notebook is largely based on Dr Magnus Palmblad's KNIME workflow, which can be reviewed [here](https://github.com/magnuspalmblad/EuropePMC2ChEBI).

> Literature_Review_Mees_final.pdf

Final version of the complete report.
