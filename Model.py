class Model():
    
    def assignPlay(self, play):
        """
        params: string (play)

        Stores the user's choice of play inside play_choice.
        """
        pass

    def getPlay(self):
        """
        params: None

        Retrieves the value of play_choice from the class variable list.action="{{ url_for('sign') }}"
        """
        pass

    def getEmptyGrammar(self):
        """
        params: None

        Retrieves the value of the empty_grammar from the class variable list
        """
        pass
    
    def getFilledGrammar(self):
        """
        params: None

        Retrieves the value of the filled_grammar from the class variable list
        """
        pass

    def getFilledGrammar(self):
        """
        params: None

        Retrieves the value of the filled_script variable from the class variable list
        """
        pass

    def assignGrammar(self, grammar_dict):
        """
        params: dictionary (grammar_dict)

        Populates the empty_grammar variable with the grammars to fill in
        from the MadLib.
        """
        pass

    def assignScript(self, script_list):
        """
        params: list (script_list)

        Populates the empty_script variable with the unpopulated lines
        from the MadLib.
        """
        pass

    def fillGrammar(self, full_grammar_dict):
        """
        params: dictionary (full_grammar_dict)

        Populates the filled_grammar variable with the user-provided
        grammar values.
        """
        pass

    def fillScript(self):
        """
        params: None

        Populates the filled_script variable by taking the elements from
        filled_grammar and putting them in place in empty_script.
        """
        pass
