# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
# GO TO LINK AND READ ABOUT TOKENS AND ETC.
import nltk
import numpy as np
import random
import string  # to proccess standard python strings

# Getting data from the web cleaned to be read =======================================================================
f = open('chatbot.txt', 'r', errors='ignore')
raw = f.read()

raw = raw.lower()  # converts to lowercase



def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first time use only

sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words

# Pre-processing the raw text #

lemmer = nltk.stem.WordNetLemmatizer()


# Wordnet is a semantically- oriented dictionary of English included in NLTK

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)



# *****************************************raw text is cleaned


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

# CONVERT A COLLECTION OF RAW DOCUMENTS TO A MATRIX OF TF-IDF FEATURES
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

# to convert a collection of raw documents to a matrix of TF-IDF features.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# response which searches the user’s utterance for one or more known keywords and returns one of several possible
# responses. If it doesn’t find the input matching any of the keywords, it returns a response:” I am sorry! I don’t
# understand you”

def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


# we will feed the lines that we want our bot to say while starting and ending a conversation depending upon the user’s input.
flag = True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while flag == True:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("ROBO: You are welcome..")
        else:
            if greeting(user_response) != None:
                print("ROBO: " + greeting(user_response))
            else:
                print("ROBO: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("ROBO: Bye! take care..")




