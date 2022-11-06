import include.expression as expression

class Evaluate:
    """
    A class used to represent an expression as its current and next characters

    Attributes:

    numbers: String containg characters that may be included in numbers
    binaryops: String containg binary operation characters 

    Methods:

    prec_assoc(operation): Gets precedence and associativity level of binary operation
    arithmetic(lhs, operation, rhs): Performs arithmetic operations of the form 'lhs operation rhs'
    sub_compute(): Helper function to handle computation of sub-expressions or numeric values
    compute(): Main recursive function to handle evaluation of expression via operation precedence climbing (recursive descent)
    """

    numbers = "-0123456789."
    binaryops = "+—*/^"

    def __init__(self, exp):
        """
        Parameters:

        exp : str
            Expression to be evaluated
        """

        self.expression = expression.Expression(exp)

    def prec_assoc(self, operation):
        """
        Gets precedence and associativity level of binary operation
                
        Parameters:

        operation: string containing operation character

        Return:

        Tuple containing precedence value in 0th index and associativity level in 1st index
        """

        if (operation == "+" or operation == "—"):
            return (0, "l")
        elif (operation == "*" or operation == "/"):
            return (1, "l")
        elif (operation == "^"):
            return (2, "r")
        raise Exception("Invalid Operation")
    
    def arithmetic(self, lhs, operation, rhs):
        """
        Performs arithmetic operations of the form 'lhs operation rhs'
                
        Parameters:

        lhs: string containing lhs of binary operation
        operation: string containing binary operation
        rhs: string containing rhs of binary operation

        Return:

        Float result of executing operation
        """

        lhs = float(lhs)
        rhs = float(rhs)
        if (operation == "+"):
            return (lhs + rhs)
        elif (operation == "—"):
            return (lhs - rhs)
        elif (operation == "*"):
            return (lhs * rhs)
        elif (operation == "/"):
            if (rhs == 0.0):
                raise Exception("Division by Zero")
            return (lhs / rhs)
        elif (operation == "^"):
            return (lhs ** rhs)
        else:
            raise Exception("Invalid Operation")
    
    def sub_compute(self):
        """
        Helper function to handle computation of sub-expressions or numeric values

        Return:

        Returns a float after recursing through association or finding number
        """

        curr_char = self.expression.get_next_char()
        if (curr_char == "("):
            curr_val = self.compute(0)
            if (self.expression.get_curr_char() != ")"):
                raise Exception("Invalid Association")
            self.expression.get_next_char()
            return curr_val
        elif (curr_char in self.numbers):
            while (self.expression.peek_next_char() != None and self.expression.peek_next_char() in self.numbers):
                curr_char += self.expression.get_next_char()
            self.expression.get_next_char()
            return float(curr_char)
        elif (curr_char in self.binaryops):
            raise Exception("Invalid Expression")
        elif (curr_char == None):
            raise Exception("Incomplete Expression")
    
    def compute(self, curr_prec):
        """
        Main recursive function to handle evaluation of expression via operation precedence climbing (recursive descent)
                        
        Parameters:

        curr_prec: int specifying minimum precedence within the current expression

        Return:

        Float value of the result of evaluating the current expression
        """

        lhs = self.sub_compute()

        while True:
            curr_char = self.expression.get_curr_char()
            if ((curr_char == None) or (curr_char not in self.binaryops) or self.prec_assoc(curr_char)[0] < curr_prec):
                break
            
            binop = self.prec_assoc(curr_char)
            precedence = binop[0]
            associativity = binop[1]

            next_prec = precedence
            if (associativity == "l"):
                next_prec += 1

            rhs = self.compute(next_prec)

            lhs = self.arithmetic(lhs, curr_char, rhs)
        return lhs