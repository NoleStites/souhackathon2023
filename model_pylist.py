from Model import Model

class model(Model):

    def __init__(self):
        play_choice = ""
        empty_grammar = []
        empty_script = []
        filled_grammar = {}
        filled_script = []

    def assignPlay(self, play):
        """
        params: string (play)

        Stores the user's choice of play inside play_choice.
        """
        self.play_choice = play
        return True

    def getPlay(self):
        """
        params: None

        Retrieves the value of play_choice from the class variable list
        """
        return self.play_choice
    
    def getEmptyGrammar(self):
        """
        params: None

        Retrieves the value of the empty_grammar from the class variable list
        """
        return self.empty_grammar

    def getFilledGrammar(self):
        """
        params: None

        Retrieves the value of the filled_grammar from the class variable list
        """
        return self.filled_grammar
    
    def getFilledGrammar(self):
        """
        params: None

        Retrieves the value of the filled_script variable from the class variable list
        """
        return self.filled_script

    def assignGrammar(self, grammar_dict):
        """
        params: dictionary (grammar_dict)

        Populates the empty_grammar variable with the grammars to fill in
        from the MadLib.
        """
        self.empty_grammar = grammar_dict
        return True

    def assignScript(self, script_list):
        """
        params: list (script_list)
        
        Populates the empty_script variable with the unpopulated lines
        from the MadLib.
        """
        self.empty_script = script_list
        return True

    def fillGrammar(self, key_grammar_dict):
        """
        params: dictionary (full_grammar_dict)

        Populates the filled_grammar variable with the user-provided
        grammar values.
        """
        self.filled_grammar = key_grammar_dict
        return True

    def fillScript(self):
        """
        params: None

        Populates the filled_script variable by taking the elements from
        filled_grammar and putting them in place in empty_script.
        """
        filledScript = []
        keys = self.filled_grammar.keys()

        for line in self.empty_script:
            temp_line = str(line)
            newLine = temp_line

            for grammar in keys:
                # Checking to see if there is a value to replace for every line in the MadLib
                curly_string = "{REPLACE_ME}"
                temp = curly_string.replace("REPLACE_ME", grammar)
                if temp_line.count(temp) > 0:
                    newLine = temp_line.replace(temp, self.filled_grammar[grammar])
                    #newLine = temp_line.replace(temp, "Nole")
            filledScript.append(newLine)
            
        self.filled_script = filledScript
        return True
