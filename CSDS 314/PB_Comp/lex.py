"""
Author: Rohan Singh
January 29, 2023
This Python MOdule contains source code for the Lexer of our Python-based compiler
"""

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
        pass

