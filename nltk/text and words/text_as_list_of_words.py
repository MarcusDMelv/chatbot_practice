# download and run the books (start here)

"""

import nltk
nltk.download()
from nltk.book import *
"""
from nltk.book import *
from text_and_words import lexical_diversity

# Creating a list
list1 = ["call", "me", "Marcus", "."]
len(list1)

list2 = ['I', "am", "tired", "of", "working"]
len(list2)
# imported function to check diversity of the list
list1_diversity = lexical_diversity(list1)
list2_diversity = lexical_diversity(list2)

# You can add list together ( sent1-9 are all preset list)
added_list = list1 + list2
print(added_list)

# appending is when you want to add a specific word to the list
list1.append("Melvin")
print(list1)

# finding words in the text use [] and the index number of the word we are looking for
index_to_word = text4[173]
print(index_to_word)

# You can find the index of a word using this syntax
word_to_index = text4.index('awaken')
print(word_to_index)
# indexing is how you access a word of any text or more generally the text of any list


# slicing is extracting large amount of text from a list
slicing_a_list = text4[173:350]
print(slicing_a_list)

# able to print subtleties
# able to print one word from the list
print(slicing_a_list[0])

# slicing from 4: to end
print(slicing_a_list[4:])
# slice only :4
print(slicing_a_list[:4])

# assignments are variables = expression

my_assignment = ["A", "list", "of people who", "don't", "care"]
slicing_assignment = my_assignment[0:4]
print(slicing_assignment)
sort_slicing_assignment = sorted(slicing_assignment)
print(sort_slicing_assignment)
#########################################################################ALERT ALERT ALERT###############################
# turning a list into a string
trial_list = ["cool", "out", "on", "the weed bro"]

trial_list_join = ' '.join(trial_list)
print(trial_list_join)

# turning a string into a list

trial_string = "This would be crazy if it works but who knows"
trial_string_to_list = trial_string.split()
print(trial_string_to_list)
##########################################################################################################################

#################
###############
###############
# How do we show the most informative words about the topic


### Find the most frequent words of a document
# Use Frequency Distribution
most_frequent_words = FreqDist(text4)  # text 4 will be distributed
most_frequent_words_list = list(most_frequent_words)  # expression list give us a list of distinct types in text
print(most_frequent_words_list[:50])
# slicing the data to the top 50

### Words that only occur once in the doc
# Use hapaxes
# still use Frequency Distribution
# using FreqDist(text) = most_frequent_words.hapaxes()
words_that_only_occur_once = most_frequent_words.hapaxes()

string_words_that_only_occur_once = ' '.join(words_that_only_occur_once)
print(string_words_that_only_occur_once)

### Find words that are over 15 characters long
"""
Algorithm = for each word in the vocab we check if its greater then 15
(V = vocabulary) 
"""
# set the text
V = set(text1)
long_words = [w for w in V if len(w) > 15]
# change the 15 to change the length of the number
print(sorted(long_words))
# sorted then printed the long words


### Find words longer then seven and occur more then seven times
# using Frequency Distribution
top_seven = FreqDist(text5)
top_seven_text5 = sorted([w for w in set(text5) if len(w) > 7 and top_seven[w] > 7])
print(top_seven_text5)
"""
COLLOCATIONS AND BIGRAMS 

"""
#collocation is a sequence of words of that occur together unusally often
#use .collocations()
# before collocation must extract out a list of words called big ram
#must run a function called bigrams()
bigrams(["more", "is", "said", "than", "done"])
# 2nd list
[("more", "is"), ("is", "said"), ("said", "then"), ("than", "dome")]
#creating collocations
my_collocations = text4.collocation_list()
print(my_collocations)
