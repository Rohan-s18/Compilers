from lex import *
from parse import *
import sys

def main():
    print("Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer and parser.
    lexer = Lexer(input)
    parser = Parser(lexer)

    parser.program() # Start the parser.
    print("Parsing completed.")


if __name__ == "__main__":
    main()