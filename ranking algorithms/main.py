import nltk as nltk
import requests
from bs4 import BeautifulSoup
import nltk
import numpy as np
import random
import string  # to proccess standard python strings


def wiki_search():
    # website
    base_url = "https://en.wikipedia.org/wiki/"
    # users search
    search = input("Search: ")
    # url to be requested
    url = base_url + search
    wiki_page = requests.get(url)
    # beautiful soup object is being placed(html.parser is important)
    #  raw data with no html tags
    # raw_data = BeautifulSoup(wiki_page.content, 'html.parser').get_text()
    # wiki_soup_page will be used to extract paragraphs
    wiki_soup_page = BeautifulSoup(wiki_page.content, 'html.parser')
    # raw div carries all info included in the search
    raw_div = wiki_soup_page.find(id='mw-content-text').get_text()
    # data with html tags still
    wiki_div = wiki_soup_page.find(id='mw-content-text')
    # ai starts processing data
    # function to clean data
    clean_raw_data(raw_div, search)


def clean_raw_data(raw_div, search):
    # div made into a list
    raw_div_listed = raw_div.split()
    # list made into a string
    raw_data = ' '.join(raw_div_listed)
    # string of info about users search (from div_listed)
    automatic_reply = ' '.join(raw_div_listed[3:18])
    # AI replies
    print(search, ":")
    print(automatic_reply)
    # return raw div data
    return raw_data

def response(user_response):
    robo_response = ''
    return robo_response

# Able to match keywords and give out direct responses *******LIST TRAINERS****************
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)  # list from user

GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello",
                      "I am glad! You are talking to me"]  # list to users reply


def greeting(sentence):
    for word in sentence.split():  # notice split
        if word.lower() in GREETING_INPUTS:  # users input
            return random.choice(GREETING_RESPONSES)  # specific replies to users list


# ********************************************** GREETING LIST TRAINER********************************

# *****************GENERATING A RESPONSE**************************************


"""
def summer_time(wiki_search_results):
    # Imports for parser_config
    # sumy is a paragraph summarizer
    # import PlaintextParser allows data to be read
    from sumy.parsers.plaintext import PlaintextParser
    # import Tokenizer converts input text to streams of tokens, where each token is a separate word
    from sumy.nlp.tokenizers import Tokenizer
    text_format = wiki_search_results
    # parser_config = user text/that is im english
    parser_config = PlaintextParser.from_string(text_format, Tokenizer(f"english"))
    # summerTime = the class SummerTime() from file SummerTime.py
    from summy import SummerTime
    summerTime = SummerTime()
    # summer_all = the a algorithm that summarizes text
    summer_all = summerTime.lex_rank_analysis(parser_config, 2)
    # summer_all = print(), summer_all
    # summer_all = the a algorithm that summarizes text
    summer_all = summer_all + summerTime.luhn_analysis(parser_config, 1)
    # summer_all = print(), summer_all
    # summer_all = the a algorithm that summarizes text
    summer_all = summer_all + summerTime.lsa_analysis(parser_config, 1)
    # a list was created
    scrubbed = []
    # 3 different algorithms is broken down into their own sentences
    for sentence in summer_all:
        concat = str(sentence) + f"\n "
        concat.replace(f"", "   ")
        scrubbed.append(concat)
    # insert 3 sentences into the output_display scrolled_text widget
    print(summer_all)
    return summer_all
"""
# list for greetings
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)  # list from user

GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello",
                      "I am glad! You are talking to me"]  # list to users reply

# we will feed the lines that we want our bot to say while starting and ending a conversation depending upon the
# user’s input.
print("I am a SearchBot! Enter a topic and lets see what I find!")
still_running = True
while still_running:
    wiki_search()
