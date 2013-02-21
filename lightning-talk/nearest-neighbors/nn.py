import numpy, csv

########## HELPER FUNCTIONS ##########

def _normalize(arr):
    '''
    Preprocessing to normalize data items on a 0-1 scale.
    '''
    rows, cols = arr.shape
    # Basically normalizes each value as a percent of the max in a column
    for col in xrange(cols):
        arr[:,col] /= abs(arr[:,col]).max()
    return list(arr)


########## MAIN ##########

# The number of nearest neighbors we want to see
K = 10

# First open and prep the data
rawdata = csv.reader(open('data/ca_economy.csv', 'r').readlines()[1:])

data, labels = [], []
for row in rawdata:
    labels.append(row[0])
    data.append([float(i) for i in row[1:]])
data = numpy.array(data) # Convert to a numpy array

# Normalize the data so everything is on a 0-1 scale. This is hugely important
# when you're dealing with Euclidean distances
normalized_data = _normalize(data)

# We want to see the entities most similar to California
query = normalized_data[labels.index('California')]

# Set up the query vector and the whole dataset for K-nearest neighbors query
qvector = numpy.array([query]).transpose()
alldata = numpy.array(normalized_data).transpose()

# You can't get more neighbors than there are entities
ndata = alldata.shape[1]
K = K if K < ndata else ndata

# Calculate Euclidean distances between query vector and other points
# and then return the sorted indices of the closet items
sqd = numpy.sqrt(((alldata - qvector[:,:ndata]) ** 2 ).sum(axis=0))
idx = numpy.argsort(sqd) # sorting

# Return just the top K nearest neighbors
similar = []
for i in idx[:K]:
    print labels[i]