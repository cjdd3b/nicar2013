'''
cluster.py

This script demonstrates the use of the DBSCAN algorithm for finding
clusters of crimes in Columbia, Mo. DBSCAN is a density-based clustering
algorithm that finds points based on their proximity to other points in the
dataset. Unlike algorithms such as K-means, you do not need to specify the
number of clusters you would like it to find in advance. Instead, you set a
parameter, epsilon, that identifies how close you would like two points to be 
for them to belong to the same cluster.

More information here:

http://en.wikipedia.org/wiki/DBSCAN
http://scikit-learn.org/dev/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN

And there's a clean, documented implementation here for reference:

https://github.com/cjdd3b/car-datascience-toolkit/blob/master/cluster/dbscan.py
'''

import csv
import numpy as np
from scipy.spatial import distance
from sklearn.cluster import DBSCAN

# Pull in our data using DictReader
labels = ['id', 'date_time', 'incident_num', 'location', 'apt_lot', 'type_id', 'lat', 'lng']
data = csv.DictReader(open('data/columbia_crime.csv', 'r').readlines()[1:], labels)

# Separate out the coordinates, which is the only data we care about for now
coords = []
for d in data:
    try:
        coords.append((float(d['lat']), float(d['lng'])))
    except ValueError: # If the coordinates are messed up, skip them
        continue

# Scikit-learn's implemenetation of DBSCAN requires the input of a distance matrix showing pairwise
# distances between all points in the dataset.
distance_matrix = distance.squareform(distance.pdist(coords))

# Run DBSCAN. Setting epsilon with lat/lon data like we have here is an inexact science. 0.03 looked
# good after a few test runs. Ideally we'd project the data and set epsilon using meters or feet.
db = DBSCAN(eps=0.03).fit(distance_matrix)

# And now we print out the results in the form cluster_id,lat,lng. You can save this to a file and import
# directly into a mapping program or Fusion Tables if you want to visualize it.
for k in set(db.labels_):
    class_members = [index[0] for index in np.argwhere(labels == k)]
    for index in class_members:
        print '%s,%s' % (int(k), '{0},{1}'.format(*coords[index]))