from Lab2.Lab2 import ConstantsSymbolTable,IdentifiersSymbolTable
from Lab3.ProgramInternalForm import ProgramInternalForm
import re

class Scanner:

    def __init__(self, filepath):
        self.operators = ["+", "-", "*", "/", "%", "<=", ">=", "==", "!=", "<", ">", "="]
        self.separators = ["[", "]", "{", "}", "(", ")", ":", ";", ",", " ", "\n", ",", "\t"]
        self.reservedWords = ["array", "char", "const", "do", "else",  "if", "int", "of", "program", "string", "for", "while", "then", "var", "while",
                              "and", "or", "HereWeGoAgain", "PainEndsHere", "ShowMe", "StayHere"]
        self.constantST = ConstantsSymbolTable(200)
        self.identifiersST = IdentifiersSymbolTable(200)
        self.pif = ProgramInternalForm
        self.filePath = filepath

    def readFile(self):
        fileContent = ""
        # Open the file for reading
        with open(self.filePath, 'r') as file:
           for line in file:
               # Add file lines to fileContent
               fileContent = fileContent + line.strip() + "\n"
        return fileContent

    def createListOfProgramElems(self):
        try:
            content = self.readFile()
            separatorsString = ''.join(self.separators)

            tokens = re.split(f'({re.escape(separatorsString)})', content)

            # Filter out empty strings and spaces
            print(tokens)
            tokens = [token for token in tokens if token.strip()]
            print(tokens)
            return self.tokenize(tokens)
        except FileNotFoundError as e:
            print(e)

        return None

    def tokenize(self, tokens_to_be):
        resulted_tokens = []
        is_string_constant = False
        is_char_constant = False
        created_string = []
        number_line = 1
        number_column = 1

        for t in tokens_to_be:
            if t == '"':
                if is_string_constant:
                    created_string.append(t)
                    resulted_tokens.append(("".join(created_string), (number_line, number_column)))
                    created_string = []
                else:
                    created_string.append(t)
                is_string_constant = not is_string_constant
            elif t == "'":
                if is_char_constant:
                    created_string.append(t)
                    resulted_tokens.append(("".join(created_string), (number_line, number_column)))
                    created_string = []
                else:
                    created_string.append(t)
                is_char_constant = not is_char_constant
            elif t == "\n":
                number_line += 1
                number_column = 1
            else:
                if is_string_constant:
                    created_string.append(t)
                elif is_char_constant:
                    created_string.append(t)
                elif t.strip():  # Check if t is not just whitespace
                    resulted_tokens.append((t, (number_line, number_column)))
                    number_column += len(t)

        return resulted_tokens

    def scan(self):
        tokens = self.createListOfProgramElems()

        lexical_error_exists = False
        # constant (1), identifier (2), (3 - operator, 4 - separator , 5 - reserved word)
        if tokens is None:
            return

        for t in tokens:
            token = t[0]
            line, column = t[1]
            if token in self.reservedWords:
                self.pif.add((token, (-1, -1), 5))
            elif token in self.operators:
                self.pif.add((token, (-1, -1), 3))
            elif token in self.separators:
                self.pif.add((token, (-1, -1), 4))
            elif re.match(r'^(0|[-+]?[1-9][0-9]*|\'[1-9]\'|\'[a-zA-Z]\'|\"[0-9]*[a-zA-Z ]*\")$', token):
                self.constantST.insert(token)
                self.pif.add(("CONST", self.constantST.getValueIndex(token), 1))
            elif re.match(r'^var[a-zA-Z][a-zA-Z0-9]*$', token):
                self.identifiersST.insert(token)
                self.pif.add(("IDENTIFIER", self.identifiersST.getValueIndex(token), 2))
            else:
                print(f"Error at line: {line} and column: {column}, invalid token: {token}")
                lexical_error_exists = True

                if not lexical_error_exists:
                    print("Program is lexically correct!")

    def get_pif(self):
        return self.pif

    def get_constantST(self):
        return self.constantST

    def get_identifiersST(self):
        return self.identifiersST


