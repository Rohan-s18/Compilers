"""
Author: Rohan Singh
January 29, 2023
This python module contains the code to test the compiler
"""

# Imports
from lex import *

# Main function to test the compiler
def main():
    code = "LET foobar = 123"
    
    my_lexer =Lexer(code)

    #Iterating through the source code
    while my_lexer.peek() != '\0':
        print(my_lexer.curChar)
        my_lexer.nextChar()

    code = "+- */ >>= = !="
    my_lexer = Lexer(code)

    token = my_lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = my_lexer.getToken()

if __name__ == "__main__":
    main()