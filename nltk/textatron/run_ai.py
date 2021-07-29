# General Libraries
import numpy
# installing Natural Language Toolkit which processes the language spoken by Humans.
import nltk

# This tokenizer divides a text into a list of sentences
nltk.download('punkt')

# imports the "namespace" Tkinter in your namespace and import Tkinter as tk does the same, but "renames" it locally
# to 'tk' to save you typing
import tkinter as tk

# imports every exposed object in Tkinter into your current namespace.
from tkinter import *

# Specific GUI Window Tabs Libraries

# Several ttk widgets will automatically substitute for the Tk widgets. Direct benefit of using the new widgets,
# giving better look & feel across platforms.
from tkinter import ttk

# Produces a functional scroll bar in a text widget
from tkinter.scrolledtext import *

# imported class SummerTime from the file SummerTime
from SummerTime import SummerTime
# import tkinter.filedialog
# Create GUI
# Create Window
# Builds main window
# window is built named window2 (intro)
window2 = tk.Tk()
# 2nd window being build
window = tk.Tk()
# Change Main Title Here
# window Title has been named
window.title("Textatron")
window2.title("What is Textatron?")
# Change Window Size Here
# wide x tall

# Change Text color here
window.config(background='green')
window2.config(background='black')
# Add/Remove Window Tabs Here

# Set style of tabs
# ttk.Style May be used to specify a custom widget style
# style =   'window' is now able to be stacked with widgets ttk.Style()
style2 = ttk.Style(window2)
style = ttk.Style(window)



# Set location of tabs
# wn = West North
# ws = West South

# Ttk Notebook widget manages a collection of windows and displays a single window one at a time. Each child window is
# associated with a tab, which the user may select to change the currently-displayed window. style.configure allows
# window to be configured a 'lefttab' widget will be  placed in the West North of the window
style.configure('lefttab.TNotebook', tabposition='wn')
style2.configure('bottomtab.TNotebook', tabposition='wn')


# Notebook is a widget used to display many windows in a limited space
# tab_control is created to add a tab to the WN of the window
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')
tab_control2 = ttk.Notebook(window2, style='bottomtab.TNotebook')


# tab_control = ttk.Notebook(window)

# Create a  tab named 'tab_main' using
# ttk.Frame is a rectangular container for other widgets
# wrap the tab widget with a rectangular container
tab_main = ttk.Frame(tab_control)

# allow tab to be shown
tab_main2 = ttk.Frame(tab_control2)


#reused for labels

# Add a tab to window tab_control.add
# display a tab with the text 'Mission control
tab_control.add(tab_main, text='Mission Control')
# tab created and named
tab_control2.add(tab_main2, text='What is this?')



# Create GUI Labels
# Place GUI Labels

# label created named 'label_summarize' using
# label widget with a notebook widget with a rectangular container with text with padding
label_summarize = Label(tab_main, text="\nHi, I am Textatron. Let me read and then Summerize the text. Then you may review and edit.\n", padx=5, pady=5)

label_summarize_Program = Label(tab_main2, text="\nHi, I am Textatron.\nI am able to summarize alot of information into a proper size paragraph:\nFirst Copy and paste the data in the top portion\n "
                                                "Then press the button to invoke me\nThats when I do the hard work to start exit out this screen", padx=5, pady=5)

# 0,0 is top left of the window
# label widget is placed in the top left window using .grid(column=0,row=0)
label_summarize.grid(column=0, row=0)

label_summarize_Program.grid(column=5, row=0)

# removes grid geometry layout manager and uses
# the notebook widget and the set layouts instead
tab_control.pack(expand=1, fill='both')
tab_control2.pack(expand=1, fill='both')

# GUi and Layer Support Functions
# Clear entry widget

# a defined function name erase_input
# deletes input
def erase_input():
    entry.delete('1.0', END)
    erase_input()

# a defined function name erase_output
# deletes output
def erase_output():
    output_display.delete('1.0', END)
    erase_output()

# a defined function name summer_time from the SummerTime.py
def summer_time():
    # Imports for parser_config
    # sumy is a paragraph summarizer
    # import PlaintextParser allows data to be read
    from sumy.parsers.plaintext import PlaintextParser
    # import Tokenizer converts input text to streams of tokens, where each token is a separate word
    from sumy.nlp.tokenizers import Tokenizer
    # text_format = user input
    text_format = entry.get('1.0', tk.END)
    # We can use this parse format for all three when we use raw strings
    # parser_config = user text/that is im english
    parser_config = PlaintextParser.from_string(text_format, Tokenizer("english"))
    #summerTime = the class SummerTime() from file SummerTime.py
    summerTime = SummerTime()

    # summer_all = the a algorithm that summarizes text
    summer_all = summerTime.lex_rank_analysis(parser_config, 2)
    #summer_all = print(), summer_all

    # summer_all = the a algorithm that summarizes text
    summer_all = summer_all + summerTime.luhn_analysis(parser_config, 2)
    #summer_all = print(), summer_all

    # summer_all = the a algorithm that summarizes text
    summer_all = summer_all + summerTime.lsa_analysis(parser_config, 2)

    # a list was created
    scrubbed = []
    # 3 different algorithms is broken down into their own sentences
    for sentence in summer_all:
        concat = str(sentence) + "\n\n\n"
        concat.replace("", "{")
        concat.replace("", "}")
        scrubbed.append(concat)
    #insert 3 sentences into the output_display scrolled_text widget
    output_display.insert(tk.END, scrubbed)
    print("\nAbout to print summer all results\n")
    print(summer_all)

# Build Main Home Tab

# a label widget is created for the window with text 'Enter text to Summarize'
label_text_to_summarize = Label(tab_main, text='Enter Text to Summarize', padx=5, pady=5)
# label was placed using .grid
label_text_to_summarize.grid(row=1, column=0)

# entry = a scrolled text widget for the window used to accept user input
entry = ScrolledText(tab_main, height=10)
# location of the scrolled text widget using .grid
entry.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

# User Action Controls and Events

# button widget created with text 'Invoke Text-A-Tron'
# the button will run the defined function 'summer_time' when pressed
button_run = Button(tab_main, text="Invoke Tex-A-Tron", command=summer_time, width=22, bg='#25d366', fg='#fff')
# button is placed and sized using .grid
button_run.grid(row=4, column=0, padx=10, pady=10)

# button widget created with text 'Erase Input'
# button will run the defined function 'erase_input' when pressed
button_erase_input = Button(tab_main, text='Erase Input', command=erase_input, width=12, bg='#25d366', fg='#fff')
button_erase_input.grid(row=5, column=0, padx=10, pady=10)

# button widget created with text 'Erase Output'
# button will run the defined function 'erase_output' when pressed
button_erase_output = Button(tab_main, text='Erase Output', command=erase_output, width=12, bg='#25d366', fg='#fff')
# button is placed using .grid
button_erase_output.grid(row=6, column=0, padx=10, pady=10)

# Display window for summarization results

# output_display = ScrolledText widget used to show results after the
#  summer_time function is ran
output_display = ScrolledText(tab_main, height=10)
# output_display is placed using .grid
output_display.grid(row=9, column=0, columnspan=5, padx=5, pady=5)
# output_display = ScrolledText(tab_main, height=9)

# Keep window alive
window.mainloop()
