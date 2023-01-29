"""
Author: Rohan Singh
January 29, 2023
This Python MOdule contains source code for the Lexer of our Python-based compiler
"""

# Imports
import enum


# Code for the Lexer class
class Lexer:

    # init function for the Lexer clsas
    def __init__(self,input):
        
        #Getting the source 
        self.source = input + '\n' 

        #Initializing the instance fields
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    # Function to process the next character
    def nextChar(self):
        self.curPos += 1                                #Moving curPos to the next one
        if self.curPos >= len(self.source):
            self.curChar = '\0'                         #EOF
        else:
            self.curChar = self.source[self.curPos]     
    
    # Function to return the lookahead character
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'                                 #EOF
        return self.source[self.curPos+1]

    # Invalid token error message
    def abort(self, message):
        pass

    # Function to skip whitespace
    def skipWhitespace(self):
        pass

    # Function to skip a comment
    def skipComment(self):
        pass
    
    # Function that returns the next character
    def getToken(self):
        # Check the first character of this token to see if we can decide what it is.
        # If it is a multiple character operator (e.g., !=), number, identifier, or keyword then we will process the rest.
        if self.curChar == '+':
            pass	# Plus token.
        elif self.curChar == '-':
            pass	# Minus token.
        elif self.curChar == '*':
            pass	# Asterisk token.
        elif self.curChar == '/':
            pass	# Slash token.
        elif self.curChar == '\n':
            pass	# Newline token.
        elif self.curChar == '\0':
            pass	# EOF token.
        else:
            # Unknown token!
            pass
			
        self.nextChar()


# Token contains the original text and the type of token.
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.


# Enum for the type of token for token classification
class TokenType(enum.Enum):
	EOF = -1
	NEWLINE = 0
	NUMBER = 1
	IDENT = 2
	STRING = 3
	
    # Keywords.
	LABEL = 101
	GOTO = 102
	PRINT = 103
	INPUT = 104
	LET = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	REPEAT = 110
	ENDWHILE = 111
	
    # Operators.
	EQ = 201  
	PLUS = 202
	MINUS = 203
	ASTERISK = 204
	SLASH = 205
	EQEQ = 206
	NOTEQ = 207
	LT = 208
	LTEQ = 209
	GT = 210
	GTEQ = 211