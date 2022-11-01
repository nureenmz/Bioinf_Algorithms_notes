######################################################################
# A simple example of how to build a Decision Tree and Random        #
# Forest classifier using Python                                     #
# This gives a very basic outline- much more testing and development #
# of models is required to generate a well-performing model.         #
# So this is just a start...                                         #
# more detail see https://scikit-learn.org/stable/modules/tree.html  #
#                                                                    #
# Sklearn does not install well system wide so we need to install    #
# into our user area.  So run the following commands (uncommented!)
# to install the required packages
"""
python3 -m pip install  sklearn --user
python3 -m pip install  graphviz --user
python3 -m pip install  matplotlib --user
python3 -m pip install  pandas --user
"""
#  To run on MSc3 or MSc4 use "python3 random_forest.py"             #
######################################################################

#main libraries Note Graphviz need to be on the path as well
#You may need to change this if you use a different path for Graphviz

from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
import pandas as pd

# graphviz needs to be found under windows-this sets the path
# which is not set by the current installer
import os
if os.name == 'nt':
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# load the Iris data- the comes with sklearn see also (http://archive.ics.uci.edu/ml/index.php)
iris = load_iris()

# Build a decision tree classifier (sklearn 'tree' module)
# DTC is a class, can perform multi-class classification of a dataset
# clf.fit(X,Y) where 
# X = array holding training samples, shape (n_samples, n_features)
# Y = integer values of training samples class labels (n_samples,)
X = iris.data
Y = iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

# Make a plot of the tree - decisions made by the algorithm
# to classify the samples
tree.plot_tree(clf)

# Graphviz export of the above tree, coloring nodes by their class
# and use explicit variable and class names
dot_data = tree.export_graphviz(clf, out_file=None,
	feature_names=iris.feature_names,
	class_names=iris.target_names,
	filled=True, rounded=True, proportion=False, special_characters=True)

graph = graphviz.Source(dot_data, format="png")
graph.render("my_decision_tree")

## These output to screen ##
# print the label species
print("Target Names")
print(iris.target_names)

# print the names of the features
print("Feature Names (for the Data Items)")
print(iris.feature_names)

# print the top iris items
print("Data Items")
print(iris.data[1:10])

# print the iris (species) targets to predict
print("Iris species to predict")
print(iris.target)

# build a table to store the data used for classification..
data=pd.DataFrame({
    'sepal length':iris.data[:,0], #names are keys!
    'sepal width':iris.data[:,1],
   'petal length':iris.data[:,2],
    'petal width':iris.data[:,3],
    'species':iris.target
})
print("Top of Data Table")
print(data.head())

##
# This pandas table provides the means to import other dataset
# just store the data as a CSV files and load data
"""
import pandas as pd
mytab = pd.read_csv('mytab.csv')
mytab.head()
"""

# Import train_test_split function
from sklearn.model_selection import train_test_split
# Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

X = data[['sepal length', 'sepal width', 'petal length', 'petal width']]  # Features
y = data['species']  # Labels

# Split arrays or matrices into random train and test subsets
# Split dataset into training set and test set
# 60% training and 40% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4) 

# Create a RF Classifier
# RF is a meta estimator - fits n decision tree classifiers on various sub-samples of the dataset
# Uses averaging to improve predictive accuracy
# and controls for overfitting
# n_estimators is number of trees in the forest, default 100
clf = RandomForestClassifier(n_estimators=5000)

# Train the model using the training sets
clf.fit(X_train,y_train)
# Make the prediction, y_pred=clf.predict(X_test)
y_pred=clf.predict(X_test)

# Computes subset accuracy
# The set of labels predicted for a sample (y_pred) must exactly match the labels in y_true (y_test)
# normalize==True has best performance of 1
# normalize==False max return is number of samples in prediction group
# Print model accuracy
print(f"Accuracy:{metrics.accuracy_score(y_test, y_pred)}")
print(f"Number of correctly classified samples:{metrics.accuracy_score(y_test, y_pred, normalize=False)}")
print("***Completed successfully***")

