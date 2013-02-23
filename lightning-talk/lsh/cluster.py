'''
lsh.py

Locality Sensitive Hashing is an elegant algorithm that allows us to identify
clusters of similar text in linear time. Unlike the traditional concept of a hash 
in computer science, which creates an efficient lookup system by minimizing collisions,
LSH attempts to hash similar items so that the likelihood of their colliding is high.
In the newsroom, LSH is good for clustering similar documents together.

More information here: 

http://en.wikipedia.org/wiki/Locality-sensitive_hashing
http://infolab.stanford.edu/~ullman/mmds/book.pdf
http://stackoverflow.com/questions/12952729/how-to-understand-locality-sensitive-hashing
'''
import csv
from utils.lsh import Cluster, shingle

# Load up the raw data. In this case we're using pre-stemmed and processed bill text
# from California, from 2009-2012.
rawdata = csv.reader(open('data/bills.txt', 'r').readlines()[1:], delimiter='|')

# Put the bills and their numbers in separate arrays
data, labels = [], []
for row in rawdata:
    labels.append(row[0])
    data.append(row[1])

# The threshold we're setting here is basically the proportion of shingles in each piece
# of text that must overlap for them to be considered the same. It should theoretically be
# equivalent to the Jaccard similarity of the shingle sets: http://en.wikipedia.org/wiki/Jaccard_index 
cluster = Cluster(threshold=0.9)
for i in xrange(len(data)):
    # If for some reason the bill text doesn't have at least 30 characters, ignore it
    # (it's probably an error).
    if not len(data[i]) >= 30:
        continue
    # The text in each bill is shingled into overlapping chunks of 30 characters. Good description
    # here: http://en.wikipedia.org/wiki/W-shingling
    cluster.add_set(shingle(data[i], 30), labels[i])

# Now we'll loop through all the clusters and print out the matches.
for cluster in cluster.get_sets():
    if len(cluster) > 1:
        # In this case, we're only interested in substantively similar bills that appeared in multiple
        # years, so we'll only print clusters that represent at least two election cycles.
        years_in_cluster = set([bill[:4] for bill in cluster])
        if len(years_in_cluster) > 1:
            print cluster