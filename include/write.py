class Write:
    """
    A class to allow for object to write file of equations

    Method:

    write(file_name, equations): Writes equation to prediction file in the form 'expression = result'
    """

    def __init__(self):
        pass

    def write(self, file_name, equations):
        """
        Writes equation to prediction file in the form 'expression = result'
                        
        Parameters:

        file_name: string representing name of file to write to
        equations: List containing evaluated expressions
        """

        file = open(file_name, "w")
        for equation in equations:
            file.write(" = ".join(map(str, equation)) + "\n")
        file.close()