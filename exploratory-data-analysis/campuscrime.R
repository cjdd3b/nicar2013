########## SETTINGS ##########

WORKING_DIR <<- "/Users/cjdd3b/Desktop/nicar2013/exploratory-data-analysis/"

########## INITIAL SETUP ##########

# We're gonna need these later
install.packages(c("ggplot2", "plyr", "reshape", "Hmisc"))
library(ggplot2)
library(plyr)
library(reshape)

# Set your working directory to the full path of the exploratory-data-analysis folder on your machine
setwd(WORKING_DIR)
data <- read.csv("data/campus_data_2011.csv") # And now load the data

########## LOOKING AT THE WHOLE DATASET ##########

# Sometimes it helps to understand the structure of our data, so let's do that first.
structure <- str(data)

# Now let's quick get a statistical summary of each column
smry <- summary(data)

# And now we'll add a few new columns representing violent, property and total crime counts
data$violent <- rowSums(data[, c(3:8)])
data$property <- rowSums(data[, c(9:11)])
data$total <- rowSums(data[, c(12:13)])

# Now let's look at the crime rankings overall
head(data[order(data$total, decreasing=T),], 10)

# And just for kicks, watch how that changes when total crime is normalized by enrollment
head(data[order(data$total / data$total_enr, decreasing=T),], 10)

########## UNIVARIATE EXPLORATION ##########

# First let's break down the data into a format that makes it easier to visualize
reshaped.crimes <- melt(data[, c(1, 3:13)], id="instname")

# Histograms by crime. Excluding any observations of 0 here as well.
p1 <- ggplot(reshaped.crimes, aes(x=value)) + geom_bar(binwidth=5) + facet_wrap(~ variable)

# Boxplots
boxplot <- ggplot(reshaped.crimes, aes(variable, value)) + geom_boxplot()
boxplot + scale_y_log10() # We can rescale to make differences a little more clear

# Really? Some campuses had 30-plus rapes? Which ones?
head(data[order(data$forcible, decreasing=T),], 10)

########## BIVARIATE EXPLORATION ##########

data.numerics <- data[, sapply(data, is.numeric)]

# I love this command, which shows visually how all numeric variables relate to one another
pairs(data.numerics)

# Now let's see the correlation scores
cormatrix <- cor(data.numerics)

# Even better, let's visualize them
m <- melt(cormatrix)
ggplot(m, aes(X1, X2, fill = value)) + geom_tile() + scale_fill_gradient(low = "blue",  high = "yellow")

########## MULTIVARIATE EXPLORATION ##########

# Now let's look at the data as a whole. As we learned before, the data is pretty strongly
# correlated, so principal component analysis can be an effective tool here.
# More info on PCA here: http://en.wikipedia.org/wiki/Principal_component_analysis
data.pca <- princomp(data.numerics, scores=TRUE)
plot(data.pca)
biplot(data.pca)

# Let's also try a technique called Multidimensional Scaling, which tries to plot items based
# on how similar they are in Euclidean space. It's a great way of finding outliers, even if it
# requires a bit of interpretation.
d <- dist(data.numerics)
# d <- dist(data.numerics[2:13]) # See what happens when we subset the columns
fit <- cmdscale(d, eig=TRUE, k=2)
x <- fit$points[,1]
y <- fit$points[,2]
plot(x, y, type="n")
text(x, y, labels = row.names(data), cex=.7)