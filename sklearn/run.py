# imports
from sklearn import tree

# decision tree

# Using labeled data to train our model
# We are going to have our classification AI figure out
# If it looks like a car or a minivan

# Based off of 2 features:
# number of seats
# HP


# Label Data:
# 0 = a sports car
# 1 = a minivan
# [ sportscar, sportscar, minivan, minivan]
auto_training_data_labels = ["car", "car", "minivan", "minivan"]
# [Horse power, Number of seats]
# The repeat is for each of the four autos above
auto_training_data_features = [[420, 2], [500, 2], [190, 9], [150, 8]]

# Create the decision classifier
decision_tree_classifier = tree.DecisionTreeClassifier()
# train classifier with data ()
# features need to be before labels
decision_tree_classifier = decision_tree_classifier.fit(auto_training_data_features, auto_training_data_labels)

# Create an unknown item to be classifier
# This is a minivan
print(decision_tree_classifier.predict([[160, 7]]))

# Create an unknown item to be classifier
# this is a sports car
print(decision_tree_classifier.predict([[660, 4]]))
