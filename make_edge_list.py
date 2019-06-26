import csv

import time

# Make a str of the current day to add to the output file
timestr = time.strftime("%Y%m%d")
filename = "edge_list_" + timestr + ".csv"

edge = []
article_proteins = {}

# Open the CSV file
with open('proteins_22-6-19.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:

        # The first line are the columns
        # Row 1 = article id
        # Row 2 = Protein on uniprot
        # Row 3 = Protei name
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            # Add items to a dictionary so you get a dictionary with article ids as key and a list of protein as value
            if row[0] in article_proteins.keys():
                article_proteins[row[0]].add(row[2])
            else:
                article_proteins[row[0]] = {row[2]}

# Iterate over the article ids and create a an edge list of tuple with pairs of proteins
for x in article_proteins:
    for protein in article_proteins[x]:
        temp_list = article_proteins[x]
        for y in temp_list:
            if y != protein:
                edge.append((protein, y))

# Write the edge list to a csv file
with open(filename, 'w') as out_file:
    csv_out = csv.writer(out_file)
    for i in edge:
        csv_out.writerow(i)
