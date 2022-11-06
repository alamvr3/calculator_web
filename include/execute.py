import include.read as read
import include.evaluate as evaluate

class Execute:
    """
    A class used to begin execution process of an expression or file of expressions 

    Methods:

    execute_text(expression): Executes expression that is inputted via text
    execute_file(file_name): Executes expressions found within inputted file
    """

    def __init__(self):
        pass
    
    def execute_text(self, expression):
        """
        Executes expression that is inputted via text
        
        Parameters:

        expression: string containing expression

        Return:

        List containing the given expression and its result
        """
        expression = expression.replace("\n", "")
        processed_expression = self.process_exp(expression)

        evaluator = evaluate.Evaluate(processed_expression)
        result = float(evaluator.compute(-1))
        if (result.is_integer()):
            result = int(result)
        return [expression, result]

    def execute_file(self, file_name):
        """
        Executes expressions found within inputted file
        
        Parameters:

        file_name: string of file_name

        Return:

        List containing lists that contain an expression with their corresponding result
        """
        reader = read.Read()
        expressions = reader.read_file(file_name)
        equations = []

        for expression in expressions:
            expression = expression.replace("\n", "")
            processed_expression = self.process_exp(expression)
            evaluator = evaluate.Evaluate(processed_expression)
            try:
                result = float(evaluator.compute(-1))
                if (result.is_integer()):
                    result = int(result)
            except:
                result = "Err"
            equations.append([expression, result])
        return equations
    
    def process_exp(self, expression):
        """
        Processes expression by removing whitespace and handling negative numbers
        
        Parameters:

        expression: string containing expression

        Return:

        A string containing the post-process expression
        """
        illegal_preceeding = "+*/^("
        expression = expression.replace(" ", "")

        expression = expression.replace("--","+")

        processed_expression = ""
        for i in range(len(expression)):
            if ((i == 0 and expression[i] == "-") or (expression[i] == "-" and expression[i - 1] in illegal_preceeding)):
                processed_expression += expression[i]
            elif (expression[i] == "-"):
                processed_expression += "—"
            else:
                processed_expression += expression[i]
        return processed_expression