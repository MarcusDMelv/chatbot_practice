from chatterbot import ChatBot, filters
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage import StorageAdapter
import requests
from bs4 import BeautifulSoup

# uncomment to training mode / comment to go into user friendly mode
# from train_new_responses import chatbot

import logging

# imported the logging to see Bots info uncomment to see logging info
# logging.basicConfig(level=logging.INFO)

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie',
                  # bot will try not to repeat responses to the user
                  filters=[filters.get_recent_repeated_responses],
                  # SQL storage_adapters
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  # database
                  database_uri='sqlite:///database.sqlite3',
                  # logic adapters
                  # best_match
                  # default_response
                  logic_adapters=[
                      {
                          # using best match
                          'import_path': 'chatterbot.logic.BestMatch',
                          # default response ( low confidence )
                          'default_response': 'I am sorry, but I do not understand.',
                          'maximum_similarity_threshold': 0.90
                      }
                  ],
                  # modify users input
                  # removes any extra white space
                  # cleans html characters
                  preprocessors=[
                      # removes any extra whitespaces
                      'chatterbot.preprocessors.clean_whitespace',
                      # Convert escaped html characters into unescaped html characters. For example: “&lt;b&gt;”
                      # becomes “<b>”.
                      'chatterbot.preprocessors.unescape_html'
                  ],
                  #  A filter that eliminates possibly repetitive responses to prevent
                  #     a chat bot from repeating statements that it has recently said.

                  )

greeting_list = ListTrainer(chatbot)
corpus = ChatterBotCorpusTrainer(chatbot)

greeting_list.train([
    'Hello, how are you?',
    'I am doing well.',
    'That is good to hear.',
    'Thank you'
])
# second list of data to add response variations
greeting_list.train([
    'Hello, how are you?',
    'I am great.',
    'That is awesome.',
    'Thanks'
])
corpus.train(
    # greetings statements
    'chatterbot.corpus.english.greetings',
    # health statements
    'chatterbot.corpus.english.health',
    'chatterbot.corpus.custom.marcus'

)


# function for chatbot to scrape from the web
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
    automatic_reply = ' '.join(raw_div_listed[4:16])
    # AI replies
    print(search, ":")
    print(automatic_reply)
    # return raw div data
    return raw_data


still_running = True
print("Hello I am a chatbot that is able to search topics and hold a conversation. Ask me about my health ")
print("\n Type: search to search a topic \n Type: exit to exit program")

# while loop begins
while still_running:
    # create a variable for user response
    user_input = input("")
    # create a variable for AI response
    response = chatbot.get_response(user_input)
    # print response
    print(response)
    # if statement when user presses search
    if user_input == 'search' or user_input == 'Search' or user_input == 'Search!' or user_input == 'search!':
        wiki_search()
        # else if statement for when user presses exit
    elif user_input == 'exit':
        still_running = False
