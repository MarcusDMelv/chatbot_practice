# must import books and everything else you see even if its grayed out
import nltk
from nltk.book import *

# grabbing data from gutenberg
from nltk.corpus import gutenberg

# gutenberg files names
gutenberg.fileids()
emma = gutenberg.words('austen-emma.txt')
"""
Program displays 3 stats for each text: avg word len/avg sentence length/and lexical diversity score
"""
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    # avg word length
    num_words = len(gutenberg.words(fileid))
    # avg sentence length
    num_sents = len(gutenberg.sents(fileid))
    # lexical diversity score
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    # print results , fileid = title of text
    print(int(num_chars / num_words), int(num_words / num_sents), int(num_words / num_vocab), fileid)

"""
raw() gives us the data with no split up tokens
example len(gutenberg.raw('blake-poems.txt')

sents() divides the text into sentences where each sentence is a list

"""

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
print(macbeth_sentences)
print(macbeth_sentences[1037])

longest_len = max([len(s) for s in macbeth_sentences])
[s for s in macbeth_sentences if len(s) == longest_len]