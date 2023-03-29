from flask import Flask, redirect, request, url_for, render_template
from model_pylist import model

app = Flask(__name__)   # our flask application
model = model()

@app.route('/')
@app.route('/index.html')
def index():
    """
    Takes the user to the landing page of the game
    """
    return render_template('index.html')


@app.route('/grammar_choices')
def grammar_choices():
    """
    After choosing a play, takes the user to a new webpage to fill in the blanks
    """
    return render_template('grammar_choices.html', empty_grammar_vars=model.getEmptyGrammar())


def readMadLib(text_file):
    """
    This function will read and store information from the empty MabLib based on the user's play choice
    """
    madlib = open(text_file, "r")    # read from madlib file

    # Get the lines from the files and parse the script from the grammar variables
    lines = madlib.readlines()
    empty_grammar = lines[0]
    lines.pop(0)

    # Formatting the grammar list
    empty_grammar_split = empty_grammar.split("), (")
    empty_grammar_split[0] = empty_grammar_split[0][1:] # Get rid of left-most and right-most parethesis
    empty_grammar_split[-1] = empty_grammar_split[-1][:-2]
    
    parsed_grammar = []
    for var in empty_grammar_split:
        temp_list = var.split(",")
        parsed_grammar.append(temp_list)

    # Store the empty grammar and unpopulated lines into the model to be used later
    model.assignGrammar(parsed_grammar)
    model.assignScript(lines)

    madlib.close()  # finished reading the file, so close it
    return True


@app.route('/display_MadLib')
def display_MadLib():
    """
    Takes the user to a new webpage containing the finalized MadLib with their input filled in
    """
    return render_template('display_MadLib.html', line_list=model.getFilledGrammar())    


@app.route('/submit_grammar_vars', methods=['POST'])
def submit_grammar_vars():
    """
    Result location of user submitting their choices for filling in the blanks
    """
    # Taking the user-provided values and populating the grammars
    grammar_dict = {}
    for grammar in model.getEmptyGrammar():
        grammar_dict[grammar[1]] = request.form[grammar[1]]
    model.fillGrammar(grammar_dict)
    model.fillScript()  # Populate the MadLib with user entries
    
    return redirect(url_for('display_MadLib'))
    

@app.route('/choose_play', methods=['POST'])
def choose_play():
    """
    Result location of user submitting their choice of play on the landing page
    """
    # Get response form website form and fetch data from a MadLib for the chosen play
    play_choice = request.form["play"]

    # Checking which play was chosen so to grab the correct MadLib
    if play_choice == "julius_caesar":
        madlib_file = "./madlibs/madlib_1.txt"
    elif play_choice == "merchant_of_venice":
        madlib_file = "./madlibs/madlib_2.txt"
    else:
        madlib_file = "./madlibs/madlib_3.txt"


    readMadLib(madlib_file)

    model.assignPlay(play_choice)
    
    return redirect(url_for('grammar_choices'))


# Run the app upon use of the "flask run" command
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True) 
