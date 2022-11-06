from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import run_js
import include.execute as execute
import include.write as write

class Calculator:
    """
    A class used to represent Calculator web-app 

    Attributes:

    digits: string containing allowed values for numbers
    ops: string containing allowed values for operations

    Methods:

    app(): The calculator app that receives input and serves output to the user
    check_expression(expression): Used to validate that no illegal characters have been used within the expression
    """

    digits = "0123456789."
    ops = "+-*/^() "

    def __init__(self):
        pass

    def app(self):
        """The calculator app that receives input and serves output to the user"""

        if (actions("Would you like to type your expression or upload a file?",["Type", "Upload"])=="Type"):
            put_button("Main Menu",onclick=lambda: run_js('window.location.reload()'))
            while (True):
                expression = input("Type the Expression You Would Like to Evaluate:", type=TEXT, required=True, validate=self.check_expression)
                executor = execute.Execute()
                try:
                    equation = executor.execute_text(expression)
                    put_text(" = ".join(map(str, equation)) + "\n")
                except:
                    put_text(expression + " = Err\n")

        else:
            put_button("Main Menu",onclick=lambda: run_js('window.location.reload()'))
            while (True):
                file = file_upload("Upload Test Set:", accept=".txt", required=True)
                src = 'test_sets/'+file['filename']
                dest = 'predictions/'+file['filename']
                open(src, 'wb').write(file['content']) 
                executor = execute.Execute()
                equations = executor.execute_file(src)
                writer = write.Write()
                writer.write(dest, equations)
                content = open(dest, 'rb').read()  
                put_file('prediction.txt', content, 'Predictions for '+file['filename'])

    def check_expression(self, expression):
        """
        Used to validate that no illegal characters have been used within the expression
        
        Parameters:

        expression: string containing user-typed expression

        Return:

        When illegal characters are found, an error string is returned
        """

        for c in expression:
            if (c not in self.digits and c not in self.ops):
                return "Invalid character: " + c
 
calculator = Calculator()

start_server(calculator.app, port=8080, debug=False)