'''
pca.py

Principal component analysis is a linear algebra technique that, for our purposes,
typically serves as a tool for dimensionality reduction. The power of PCA from a
journalistic standpoint is that it allows us to visualize a large amount of numerical
data in order to help spot things like outliers. It does this by finding variables that
tend to correlate in the same direction and using those relationships to simplify an
otherwise high-dimensional dataset. PCA works especially well when the columns in your
dataset tend to be highly correlated.

More information about PCA can be found here:
http://en.wikipedia.org/wiki/Principal_component_analysis
'''
import csv

# Scikit-learn makes PCA (and a lot of other things) extremely easy
from sklearn import decomposition
import pylab as pl # For graphing purposes

# First let's get some data, in this case crime stats from major college campuses 
# from the Department of Education.
rawdata = csv.reader(open('data/campus_data_2011.csv', 'r').readlines()[1:])

# Process the data into a 2D array, omitting the header row
data, labels = [], []
for row in rawdata:
    labels.append(row[0])
    data.append([int(i) for i in row[1:]])

# Set up our PCA. We only want the first two principal components so we can visualize
# the results on a 2-D plot.
pca = decomposition.PCA(n_components=2)
pca.fit(data)

# Now transform our data using PCA
X = pca.transform(data)

# And now we'll plot the results, with each of the two principal components on an axis
for i in range(len(X)):
    pl.plot(X[i, 0], X[i, 1], marker='o', markersize=10, label=i)
    pl.text(X[i, 0], X[i, 1], i, fontsize=11)
pl.show()