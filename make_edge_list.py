import csv
import time
import collections

# Make a str of the current day to add to the output file
timestr = time.strftime("%Y%m%d")
filename = "edge_list_" + timestr + ".csv"

edge = []
occurrences = collections.defaultdict(int)
article_proteins = {}

# Open the CSV file
with open('proteins_1_7_19.csv') as csv_file:
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
            # Add items to a dictionary so you get a dictionary with article ids as key and a list of protein as value
            if row[0] in article_proteins.keys():
                article_proteins[row[0]].add(row[2])
            else:
                article_proteins[row[0]] = {row[2]}

# Iterate over the article ids and create a an edge list of tuple with pairs of proteins
amount_to_many = 0
amount_used = 0
total_articles = len(article_proteins.keys())
threshold = 100
for x in article_proteins:
    if(len(article_proteins[x]) < threshold):
        amount_used += 1
        for protein in article_proteins[x]:
            temp_list = article_proteins[x]
            interactions_set = set()

            for y in temp_list:
                if y != protein:
                    interaction = (protein, y)
                    interactions_set.add(interaction)
    else:
        amount_to_many += 1

    for y in interactions_set:
        edge.append(y)
print(f'First thise were amount of interactions:{len(edge)}')

# Make a dictionary that counts the occurrences  and then make a list of proteins that occurs more than the treshold
# Based on this answer: https://stackoverflow.com/questions/1285468/python-filter-a-list-to-only-leave-objects-that-occur-once
for y in edge:
    occurrences[y] += 1
edge[:] = [x for x in occurrences if occurrences[x] > 2]
test = []
test[:] = [x for x in occurrences if occurrences[x] == 1]
print(f'This amount of interactions occured once and were removed{len(test)}')
print(f'This is the amount of interactions left {len(edge)}')


print(
    f'Treshold of {threshold} results in {amount_used} used and {amount_to_many} not used of {total_articles} articles.')


# Write the edge list to a csv file
with open(filename, 'w') as out_file:
    csv_out = csv.writer(out_file)
    for i in edge:
        csv_out.writerow(i)
