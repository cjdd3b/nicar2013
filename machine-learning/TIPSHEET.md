Practical machine learning (in the newsroom)
==========================================

Below we've included some resources and advice you can use to get started with machine learning in the newsroom.

## Algorithms

In a totally oversimplified way, machine learning algorithms can be broken down into two categories: **supervised** and **unsupervised**.

Supervised algorithms are typically responsible for classification. Given a bunch of training examples, supervised algorithms can look at a previously unseen observation and classify it into the correct group. Say you've got a bunch of bills and you want to know which ones are about the environment. If you show an algorithm enough examples of environment-related and not-environment-related bills, it can learn the difference between the two and separate them accordingly.

If classifying bills sounds pretty useless, keep in mind that **some of data journalism's hardest problems are classification problems in disguise**. Want to extract an address from a string of text in a more flexible way than regular expressions will allow? Classification problem. Want to figure out whether two campaign contribution records likely come from the same donor? Classification problem. Want to extract quotes from news stories, and then separate them into direct vs. indirect statements? Classification problem. In fact, many hard data cleaning tasks can be turned into classification problems with a little creativity.

On the other side, unsupervised learning is often used for clustering and spotting outliers. Given a bunch of data, unsupervised algorithms can sort them into groups and/or find entries that don't belong. This can be a great tool inside the newsroom, where many stories are based on either trends or outliers.

### Supervised algorithms

Some algorithms are obviously easier to understand than others. The following is a list of several common supervised learning algorithms, ordered by Chase's perceived usefulness and degree of difficulty. If you're going to learn this stuff, consider starting at the top and working your way down.

1. Linear regression
2. Logistic regression
3. Naive Bayes
4. Nearest neighbors
5. Decision trees
6. Ensemble decision trees (Random Forests)
7. Neural networks
8. Support Vector Machines

### Unsupervised algorithms

Unlike the supervised algorithms above, these unsupervised algorithms perform a variety of different tasks, from clustering to [dimensionality reduction](http://en.wikipedia.org/wiki/Dimension_reduction) for the purposes of outlier detection and visualization. Again, consider starting at the top and working your way down.

1. K-Means clustering (clustering)
2. Principal Component Analysis (dimensionality reduction)
3. DBSCAN (clustering)
4. Hierarchical clustering (clustering)
5. Multidimensional Scaling (dimensionality reduction)

## Background material and theory

Although you can get a long way using out-of-the-box algorithms from various programming libraries, doing machine learning well requires an understanding of some mathematical and statistical theory, as well as some practical advice for applying the algorithms and evaluating their results.

Machine learning is heavy on statistics and linear algebra. You might have some familiarity with statistics, but linear algebra expertise is much less common around the newsroom. If you have time, it's worth checking out Andrew Ng's famous Stanford machine learning class, which is [available on Coursera](http://ml-class.org). If you're in a rush, consider checking out the following lectures:

- [Supervised](https://class.coursera.org/ml/lecture/preview_view/3) and [unsupervised](https://class.coursera.org/ml/lecture/preview_view/4) learning -- Provides a useful intro to both primary types of machine learning algorithms.
- Linear regression [model representation](https://class.coursera.org/ml/lecture/preview_view/5) and [cost function](https://class.coursera.org/ml/lecture/preview_view/6) -- Introduces the idea of a cost function as it applies to a relatively basic algorithm in linear regression. You'll see cost functions pop up a lot.
- Intro to [logistic regression](https://class.coursera.org/ml/lecture/preview_view/33) -- Shows how a cost function applies to classification.
- [K-means](https://class.coursera.org/ml/lecture/preview_view/78) -- Basic intro to a very common and easy-to-understand clustering algorithm.
- Intuition behind [dimensionality reduction](https://class.coursera.org/ml/lecture/preview_view/82) -- Introduces the concept of dimensionality reduction, which is pretty foreign in the CAR world.
- Basics of [Principal Component Analysis](https://class.coursera.org/ml/lecture/preview_view/85) -- Introduces a simple dimensionality reduction trick that has some useful applications for data exploration in CAR.

Equally important is knowing how to evaluate the results of your algorithms. The following lectures offer some of the most valuable practical machine learning advice you will ever hear. Watch them before you go too far down the rabbit hole.

- [Model selection and train/validation/test sets](https://class.coursera.org/ml/lecture/preview_view/610)
- [Bias vs. variance](https://class.coursera.org/ml/lecture/preview_view/62)
- [Learning curves](https://class.coursera.org/ml/lecture/preview_view/64)
- [Deciding what to try next](https://class.coursera.org/ml/lecture/preview_view/65)


## Standalone software

With the explosion of Big Data in Silicon Valley, it should come as no surprise that very smart people have developed useful software that's great for getting started with machine learning. You can get a lot of mileage from these out-of-the-box implementations, particularly for some of the modest machine learning tasks we're just starting to see pop up in the newsroom.

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

