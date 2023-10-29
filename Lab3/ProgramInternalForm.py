


class ProgramInternalForm:
    def __init__(self):
        # Holds token/identifier/constant + the position in the symbol table
        self.tokenPositionPair = []
        # Holds the category of the token -
        # constant (1), identifier (2), (3 - operator, 4 - separator , 5 - reserved word)
        self.types = []

    def add(self, pairToAdd, typeToAdd):
        self.types.append(typeToAdd)
        self.tokenPositionPair.append(pairToAdd)


    def __str__(self):
        computedString = ""
        for i in range(len(self.tokenPositionPair)):
            computedString = computedString + self.tokenPositionPair[i][0] + " - " + self.tokenPositionPair[i][1] + " -> " + str(self.types[i]) + "\n"
        return computedString



