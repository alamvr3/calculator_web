class Read:
    """
    A class to allow for object to read file of expressions
    
    Method:

    read_file(file_name): Reads file and collects expressions from within
    """

    def __init__(self):
        pass

    def read_file(self, file_name):
        """
        Reads file and collects expressions from within
                
        Parameters:

        file_name: string containing file name

        Return:

        List containing the expressions found within the file
        """

        file = open(file_name, "r")
        expressions = []
        while True:
            currLine = file.readline()
            if (currLine == "\n"):
                continue
            if not currLine:
                break

            expressions.append(currLine)
        file.close();
        return expressions