'''
mds.py

Along with PCA, Multidimensional Scaling is another way of reducing the dimensionality
of a dataset so it can be visualized in order to find things like outliers. It does this
by measuring the Euclidean distances between each item in your dataset and then mapping them
to a 1-, 2-, or 3-dimensional space for the purposes of visualization.
'''
import csv
import numpy as np

# Scikit-learn makes PCA (and a lot of other things) extremely easy
from sklearn import manifold
from sklearn.metrics import euclidean_distances
import pylab as pl # For graphing purposes

# First let's get some data, in this case crime stats from major college campuses 
# from the Department of Education.
rawdata = csv.reader(open('data/campus_data_2011.csv', 'r').readlines()[1:])

# Process the data into a 2D array, omitting the header row
data, labels = [], []
for row in rawdata:
    labels.append(row[0])
    data.append([int(i) for i in row[1:]])

# Calculate the similarity matrix between all the rows
similarities = euclidean_distances(data)

# Now run very basic MDS
# Documentation here: http://scikit-learn.org/dev/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS
mds = manifold.MDS(n_components=2, dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_

# Plot the points
for i in range(len(pos)):
    pl.plot(pos[i, 0], pos[i, 1], marker='o', markersize=10, label=i)
    pl.text(pos[i, 0], pos[i, 1], i, fontsize=11)
pl.show()