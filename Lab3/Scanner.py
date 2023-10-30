from Lab2.Lab2 import ConstantsSymbolTable,IdentifiersSymbolTable

import re

class Scanner:

    def __init__(self, filepath):
        self.operators = ["+", "-", "*", "/", "%", "<=", ">=", "==", "!=", "<", ">", "="]
        self.separators = ["[", "]", "{", "}", "(", ")", ":", ";", ",", " ", "\n", ",", "\t", "\""]
        self.reservedWords = ["array", "char", "const", "do", "else",  "if", "int", "of", "program", "string", "for", "while", "then", "var", "while",
                              "and", "or", "HereWeGoAgain", "PainEndsHere", "ShowMe", "StayHere"]
        self.constantST = ConstantsSymbolTable(200)
        self.identifiersST = IdentifiersSymbolTable(200)
        self.pifOutput = []

        self.filePath = filepath

    def readFile(self):
        fileContent = ""

        # Open the file for reading
        with open(self.filePath, 'r') as file:
           for line in file:

               # Add file lines to fileContent
               fileContent = fileContent + line.strip() + "\n"

        return fileContent

    def getProgramTokens(self):
        try:

            content = self.readFile()
            # Initialize variables to store tokens
            tokens = []
            local_word = ""
            in_quoted_string = False

            # Process content character by character
            for char in content:
                if in_quoted_string:
                    local_word += char
                    if char == '"':
                        in_quoted_string = False
                elif char not in self.operators and char not in self.separators and char not in self.reservedWords:
                    local_word += char  # If char is not in the operators, separators, or reserved words, we add it to form the word
                else:
                    if local_word:
                        tokens.append(local_word)  # Add the word
                        local_word = ""
                    if char == '"':
                        local_word = '"'
                        in_quoted_string = True
                    elif char.strip() or char in self.operators or char in self.separators or char in self.reservedWords:
                        tokens.append(char)  # Add the separator, even if the word is empty

            # If there's any remaining word after processing the content
            if local_word:
                tokens.append(local_word)
            # Filter out '\n' strings
            #tokens = [token for token in tokens if token != '\n']

            return tokens

        except FileNotFoundError as e:
            print(e)

        return None

    def scan(self):
        tokens = self.getProgramTokens()
        counter = 1
        if tokens is None:
            return
        for t in tokens:
            token = t
            if token == "\n":
                counter += 1
            elif token in self.reservedWords:
                newIndex = self.find_token_index(token)
                self.pifOutput.append([newIndex,  "0"])
            elif token in self.operators:
                newIndex = self.find_token_index(token)
                self.pifOutput.append([newIndex, "0"])

            elif token in self.separators:
                newIndex = self.find_token_index(token)
                self.pifOutput.append([newIndex, "0"])

            elif re.match(r'^(0|[-+]?[1-9][0-9]*|\'[1-9]\'|\'[a-zA-Z]\'|\"[0-9]*[a-zA-Z ]*\"|".*\s*")$', token):
                if self.constantST.search(token) == -2:
                    self.constantST.insert(token, self.constantST.__len__())
                self.pifOutput.append(["CONSTANT", self.constantST.getPositionPair(token)])
            elif re.match(r'^var[a-zA-Z][a-zA-Z0-9]*$', token):
                if self.identifiersST.search(token) == -2:
                    self.identifiersST.insert(token, self.identifiersST.__len__())

                self.pifOutput.append(["IDENTIFIER", self.identifiersST.getPositionPair(token)])
            else:
                print(f"Invalid token: {token} on line {counter}")
                lexical_error_exists = True
                if not lexical_error_exists:
                    print("Program is lexically correct!")



    def find_token_index(self, target_token):
        with open('token.in', 'r') as file:
            for line in file:
                line = line.strip()
                if target_token in line:
                    index = line.split()
                    return index[0]

    def get_pif(self):
        return self.pifOutput

    def get_constantST(self):
        return self.constantST

    def get_identifiersST(self):
        return self.identifiersST


