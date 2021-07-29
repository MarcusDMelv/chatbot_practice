import wikipedia
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from gtts import gTTS


#This module is imported so that we can play
# converted into audio
import os

"""
#TEXTBASED aiWIKI 
search_phase = input("Type in a search phrase")
output_sentences = input("How many sentences would you like to output?")
output_phase = wikipedia.summary(search_phase, sentences=output_sentences)
print(output_phase)
"""

# GUI
window = tk.Tk()
#title
window.title("AI Speaker")
#size full screen
#window.geometry('1200x1200')

#better GUI
style = ttk.Style(window)

#tab
style.configure('lefttab.TNotebook', tabposition='wn')
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')
tab_main = ttk.Frame(tab_control)
tab_control.add(tab_main, text='AI Speaker')

# Brief summary label
label_summarize = Label(tab_main, text="\nSummary: Type a topic to search and then AI will speak on the topic.\n", padx=5, pady=5)
label_summarize.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

# ai is created
def ai_creator():
 # the text that you converted to audio uncomment
 # myText = ''
 # file input audio
 myText = open("ai.txt", "r").read().replace("\n", " ")
 # language
 language = 'en'
 # Passing the text and language and text to the engine
 # here we have slow = False. which tells the
 # module that the converted audio should
 # have high speed
 myobj = gTTS(text=myText, lang=language, slow=False)
 # saving the converted audio in mp3 file named
 # welcome
 myobj.save("aiSpeaking.mp3")
 #Playing the converted file
 os.system("start aiSpeaking.mp3")
#erase text function

#erase input
def erase_input():
 #entries
 #entry_sentences.delete('1.0', END)
 entry.delete('1.0', END)
 print("About to Erase input:")
 erase_input()

#erases out out
def erase_output():
 #entries
 output_display.delete('1.0', END)
 print("About to erase output:")
 erase_output()

#create aiTXT
def wikiTXT_output():
 #uai accepts user text
 search_phrase2 = entry.get('1.0', tk.END)
 #ai searches########################################################
 output_phrase = wikipedia.summary(search_phrase2, sentences=200)
 ###############################################################3####
 #ai open file
 file = open("ai.txt", "w")
 # ai writes output in a file
 file.write(output_phrase)
 # closes file
 file.close()
 #shows in outputdisplay
 output_display.insert(tk.END, output_phrase)
 print(output_phrase)


#search wiki function
def wiki_output():
 #entries
 search_phrase = entry.get('1.0', tk.END)
 #number of sentences uncomment code below
 #output_sentences = entry_sentences.get('1.0',tk.END)
 #tried to get a summary from wiki
 #output_phrase = print(wikipedia.summary(search_phrase))
 #tried to get summary summary from wiki
 #outpt_phrase = print(wikipedia.page(search_phrase).content)
 #
 #
 #
 #
 output_phrase = wikipedia.summary(search_phrase, sentences=200)
 #
 #
 #
 #
 #open file / write in file
 file = open("ai.txt", "w")
 #ai writes output in a file
 file.write(output_phrase)
 #closes file
 file.close()
 # ai speaks
 ai_creator()
# this syntax gives whole summary
# wikipedia.summary("")
 output_display.insert(tk.END, output_phrase)




 print("About to print speech:")
 print(output_phrase)



# a label widget is created for what topic to search
label_text_to_summarize1 = Label(tab_main, text='Enter a topic for the AI to speak about: ', padx=5, pady=5)
# label was placed using .grid
label_text_to_summarize1.grid(row=1, column=0)

#user input for topic
entry = ScrolledText(tab_main, height=0) # location of the scrolled text widget using .grid entry.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
# location of the scrolled text widget using .grid
entry.grid(row=1, column=0, columnspan=5, padx=5, pady=5)


# a label widget is created for how many sentences
#label_text_to_summarize2 = Label(tab_main, text='How many sentences:', padx=5, pady=5)
# label was placed using .grid
#label_text_to_summarize2.grid(row=3, column=0)

#user input for how many sentences
#entry_sentences = ScrolledText(tab_main, height=0)
# location of the scrolled text widget using .grid
#entry_sentences.grid(row=4, column=0, columnspan= 5, padx= 5, pady= 5)

#button created to activate voic
button_run = Button(tab_main, text="AI Speak", command=wiki_output, width=22, bg='#25d366', fg='#fff')
# button is placed and sized using .grid
button_run.grid(row=5, column=0, padx=5, pady=5)

#button created to activate txt
#button_run = Button(tab_main, text="AI Text", command=wikiTXT_output, width=22, bg='#25d366', fg='#fff')
# button is placed and sized using .grid
#button_run.grid(row=6, column=0, padx=5, pady=5)


#button created to erase output
button_run = Button(tab_main, text="Erase Input", command=erase_input, width=22, bg='#25d366', fg='#fff')
# button is placed and sized using .grid
button_run.grid(row=5, column=1, padx=5, pady=5)

#button created to erase input
button_run = Button(tab_main, text="Erase Output", command=erase_output, width=22, bg='#25d366', fg='#fff')
# button is placed and sized using .grid
button_run.grid(row=5, column=2, padx=5, pady=5)


# a label widget is created for the window with text 'Enter text to Summarize'
label_text_to_summarize3 = Label(tab_main, text='AI Text OUTPUT::', padx=5, pady=5)
# label was placed using .grid
label_text_to_summarize3.grid(row=7, column=0)

#out put AI WIKI results
output_display = ScrolledText(tab_main, height=30, width=200)
# output_display is placed using .grid
output_display.grid(row=8, column=0, columnspan=5, padx=5, pady=5)

#needed for GUI
window.mainloop()