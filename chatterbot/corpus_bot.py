from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# able to train bot from a list now
from chatterbot.trainers import ListTrainer
# access to bot logs
import logging

# creating logger variable
logger = logging.getLogger()

# will only out put critical information

# if uncomment will output low level warnings
# https://github.com/gunthercox/ChatterBot/blob/master/examples/learning_feedback_example.py
logger.setLevel(logging.CRITICAL)

# if uncomment shows logging info Ai is doing (proof of training)
logging.basicConfig(level=logging.INFO)
'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

bot = ChatBot('corpus', preprocessors=['chatterbot.preprocessors.clean_whitespace',
                                       'chatterbot.preprocessors.unescape_html'],
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri=None,

              logic_adapters=[
                  'chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.TimeLogicAdapter',
                  'chatterbot.logic.BestMatch'
              ]
              )

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    "chatterbot.corpus.english.greetings",
     "chatterbot.corpus.english.conversations"
)
print("Lets Talk")
while True:
    try:
        # Triggers users input
        print("I got this! ")
        user_input = input("")
        # response to user text
        response = bot.response_selection.get_most_frequent_response(user_input)
        # AI ask if response is correct

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
