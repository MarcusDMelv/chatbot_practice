"""
# download and run the books (start here)
fownload all the books
import nltk
nltk.download()

"""

from nltk.book import *

print("**************************Concordance****************************************")
# shows occurrence around the word in ("") Search text
print("Monstrous")
text1.concordance("monstrous")
print("Affection")
text2.concordance("affection")
print("Lived")
text3.concordance("lived")

print("**************************Similar****************************************")
# show words similar to the word in ("") search text
print("Monstrous")
text1.similar("monstrous")
print("Affection")
text2.similar("affection")
print("Lived")
text3.similar("lived")

print("**************************Common_Context****************************************")
# shows context shared by two or more words
text2.common_contexts(["monstrous", "very"])

print("**************************Generate text from specific location***************************************")
# generated random text
text4.generate()


print("**************************Counting Data Tokens**************************************************************")
number_of_tokens_text4 = len(text4)
print(number_of_tokens_text4)  # tokens
# Total number of tokens in ()


print("******************************Display All tokens************************************************************")
# this will show all the tokens in the ()
show_all_tokens_text4 = set(text4)
print(show_all_tokens_text4)

print("******************************Sorted Tokens*******************************************************************")
# this will sort the tokens alphabetically Uppercase shown before lowercase
show_all_tokens_sorted_text4 = sorted(set(text4))
print(show_all_tokens_sorted_text4)
print("******************************Number of Unique Item Types***************************************************")
# unique item types are actual spelled words from a certain location
number_of_tokens_text4_sorted = len(set(text4))
print(number_of_tokens_text4_sorted)
# actual number of words in document

print(
    "****************************Formula to see how many times each word is used*************************************")
word_in_a_doc_count = len(text4) / len(set(text4))
# use this formula to check data
print(word_in_a_doc_count)
# each word is used about 15 times)

print("********************Count how many times a word is being used in the text*********************")
specific_word_count = text4.count("discrediting")
print(specific_word_count)

print("**********************Find the percentage of text is being used by a word*****************************")
percentage_word_is_being_used = 100 * text4.count('a') / len(text4)
print(percentage_word_is_being_used)

print("********* FUNCTIONS / How many times one word is being used/ How much of the text is that word being used in %")


# how many times is a word being used
def lexical_diversity(text):
    return len(text) / len(set(text))


# specific word being used
def percentage(count, total):
    return 100 * count / total


# using functions to see how many times each word is used and to see a specific word being used

diversity_function = lexical_diversity(text4)
percentage_function = percentage(text4.count('a'), len(text4))
print(percentage_function, diversity_function)
