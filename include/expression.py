class Expression:
    """
    A class used to represent an expression as its current and next characters

    Attributes:

    expression: string representing the given expression
    curr_index: int representing current index of next character
    len_expression: int representing length of given expression

    Methods:

    getNextChar(): Gets next character of expression
    getCurrChar(): Gets current character of expression
    peekNextChar(): Gets next character of expression by peeking forward without changing curr_index
    """
    def __init__(self, expression):
        """
        Parameters:

        expression : str
            Expression to be iterated through
        """

        self.expression = expression
        self.curr_index = 0
        self.len_expression = len(expression)
    
    def get_next_char(self):
        """
        Gets next character from expression

        Return:

        Next character in expression if there are anymore, otherwise it returns None
        """

        if (self.curr_index < self.len_expression):
            next_token = self.expression[self.curr_index]
            self.curr_index += 1
            return(next_token)
        else:
            return None

    def get_curr_char(self):
        """
        Gets current character from expression
        
        Return:

        Current character in expression if there are anymore, otherwise it returns None
        """

        if ((self.curr_index - 1) < self.len_expression):
            return(self.expression[self.curr_index - 1])
        else:
            return None

    def peek_next_char(self):
        """
        Returns next character from expression by peeking forward
        
        Return:

        Next character in expression if there are anymore, otherwise it returns None
        """

        if ((self.curr_index) < self.len_expression):
            return(self.expression[self.curr_index])
        else:
            return None