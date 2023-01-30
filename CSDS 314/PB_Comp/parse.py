import sys
from lex import *

# Parser object keeps track of current token and checks if the code matches the grammar.
class Parser:
    def __init__(self, lexer):
        pass

    # Return true if the current token matches.
    def checkToken(self, kind):
        pass

    # Return true if the next token matches.
    def checkPeek(self, kind):
        pass

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        pass

    # Advances the current token.
    def nextToken(self):
        pass

    def abort(self, message):
        sys.exit("Error. " + message)
        