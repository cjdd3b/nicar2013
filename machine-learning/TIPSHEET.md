Practical machine learning (in the newsroom)
==========================================

Below we've included some software and code libraries you can use to get started with machine learning in the newsroom.

## Standalone software

- [Apache Mahout](http://mahout.apache.org/) -- Mahout has gained a lot of momentum recently as a scalable toolkit for doing large-scale machine learning over distributed networks. Many common algorithms are implemented, and it can easily be run on an individual laptop for smaller tasks. Also has great documentation and tutorials.
- [Weka](http://www.cs.waikato.ac.nz/ml/weka/) -- A well-established open source data mining toolkit. Comes with a GUI!
- [Mallet](http://mallet.cs.umass.edu/) -- A Java-based toolkit focused on machine learning's applications to natural language processing. Has functions for document clustering, topic modeling, information extraction and other common tasks.

## Code libraries and other resources

Useful machine learning libraries have been implemented in most common languages, although their support and adoption varies. For the kind of smaller-scale
work you're likely to do in the newsroom, data scientists most often use Python and R.

### Python

- [Scikit-learn](http://scikit-learn.org/stable/) (Python) -- An extensive, well-supported library containing implementations for most commonly used algorithms (and a few uncommon ones). Probably the best place to start for machine learning in Python.
- [NLTK](http://nltk.org/) (Python) -- The Natural Language Toolkit is the go-to library for natural language processing in Python. Comes with tools for tasks like document classification and clustering. It also helps a ton with common preprocessing tasks.
- [Numpy](http://www.numpy.org/) (Python) -- Not a machine learning library, per se, but a dependency for most of them. Numpy is also your go-to toolkit for dealing with matrices and linear algebra, which can be useful when implementing your own algorithms.
- [PANDAS](http://pandas.pydata.org/) -- The Python Data Analysis Library is a relatively young but nonetheless mature project designed for doing high-end, R-style data analysis in Python.
- [Matplotlib](http://matplotlib.org/) -- The go-to library for graphing and plotting in Python.
- [iPython](http://ipython.org/) -- An interactive computing library popular with data scientists.

### R

R has dozens of libraries to cover various machine learning functions, but some of the best are laid out here:

- [Machine Learning for Hackers](http://shop.oreilly.com/product/0636920018483.do) -- Probably the best introduction to machine learning and data science using R. Also, [the code](https://github.com/johnmyleswhite/ML_for_Hackers) is available on Github.
- [Machine learning demos in R](http://i2pi.com/rez/ml_talk/ml_demo.R) -- A popular demo written a few years ago by Josh Reich, now the founder and CEO at Simple.


### Ruby

- [Mahout + JRuby](http://www.vasinov.com/blog/machine-learning-with-ruby-part-one) (Ruby) -- A useful tutorial showing how to hook Ruby and Mahout together.