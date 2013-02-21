'''
classify.py

This script demonstrates the use of a Random Forest for classifying what
category a piece of legislation belongs to, based on the words in its title.
Random Forests are sort of a like a democratic implementation of decision trees.
A number of trees are instantiated using various criteria to make sure they
represent a range of possible views on the data. Each of those trees then votes
on the proper way to classify a given item. The highest-scoring classification
is then used. More info here:

http://en.wikipedia.org/wiki/Random_forest
http://scikit-learn.org/dev/modules/ensemble.html

You can also look here for another example of a Random Forest in action for a
journalistic purpose:

https://github.com/cjdd3b/fec-standardizer/wiki
'''
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn import cross_validation

########## HELPER FUNCTIONS ##########

def clean(text):
    '''
    A function for cleaning up the input text. Ideally we'd strip things like punctuation
    here, but instead we're just being lazy and lowercasing all input strings.
    '''
    return text.lower()

########## MAIN ##########

# First we'll load in our bill data, which comes from Sunlight's OpenStates project.
# In this case, we're using California bills.
rawdata = csv.reader(open('data/ca_bills.csv', 'r').readlines()[1:])

# Now we'll split the actual bill titles and their correct categories into two separate
# arrays. This is standard preprocessing for scikit-learn.
billtext, labels = [], []
for row in rawdata:
    # If the bill doesn't have a category assigned, we'll ignore it. Just makes things
    # cleaner for this example.
    if row[1]:
        billtext.append(clean(row[0])) # Clean the text using the above function
        # Add the correct classification to the labels array. In this case, if there
        # are multiple categories under which the bill can be classified, we just use
        # the first (again, for simplicity).
        labels.append(row[1].split('|')[0])

# Now we'll do some preprocessing in scikit-learn. Namely, we're going to take our bill titles
# and convert them into sparse tf-idf vectors, which you can read more about here:
# http://en.wikipedia.org/wiki/Tf%E2%80%93idf
# http://pyevolve.sourceforge.net/wordpress/?p=1589
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(billtext)
tf_transformer = TfidfTransformer().fit(X_train_counts)
training_data = tf_transformer.transform(X_train_counts)

# Scikit-learn expects the class labels fed to it in training to be integers, so here's a little
# hack to convert our category labels into numbers.

# First, we make a list of all the distinct categories in the dataset.
distinct_labels = list(set(labels))

# And second, we create a copy of the original labels array that replaces the text labels with
# their index positions in the distinct_labels array we just created.
correct_labels = [distinct_labels.index(l) for l in labels]

# It literally takes two lines of code to build and train a Random Forest. Feel free to mess with
# the parameters, which are outlined here: http://scikit-learn.org/dev/modules/generated/sklearn.ensemble.RandomForestClassifier.html
clf = RandomForestClassifier(n_estimators=10, random_state=0)
clf = clf.fit(training_data.toarray(), correct_labels)

# Now we'll feed in a couple new examples and see how it does
docs_new = ["Public postsecondary education: executive officer compensation.",
            "An act to add Section 236.3 to the Education code, related to the pricing of college textbooks.",
            "Political Reform Act of 1974: campaign disclosures.",
            "An act to add Section 236.3 to the Penal Code, relating to human trafficking."
        ]
X_new_counts = count_vect.transform(docs_new)
test_data = tf_transformer.transform(X_new_counts)

# And it classifies that example as "Crime", which looks correct!
for i in xrange(len(docs_new)):
    print '%s -> %s' % (docs_new[i], distinct_labels[clf.predict(test_data.toarray()[i])])