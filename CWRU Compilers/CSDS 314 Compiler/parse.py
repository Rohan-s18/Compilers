import sys
from lex import *

# Parser object keeps track of current token and checks if the code matches the grammar.
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()    # Call this twice to initialize current and peek.

    # Return true if the current token matches.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()

    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No need to worry about passing the EOF, lexer handles that.


    def abort(self, message):
        sys.exit("Error. " + message)

    # program ::= {statement}
    def program(self):
        print("PROGRAM")

        # Parse all the statements in the program.
        while not self.checkToken(TokenType.EOF):
            self.statement()

    # One of the following statements...
    def statement(self):
        # Check the first token to see what kind of statement this is.

        # "PRINT" (expression | string)
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                # Simple string.
                self.nextToken()
                # "IF" comparison "THEN" {statement} "ENDIF"
            elif self.checkToken(TokenType.IF):
                print("STATEMENT-IF")
                self.nextToken()
                self.comparison()

                self.match(TokenType.THEN)
                self.nl()
                # Zero or more statements in the body.
                while not self.checkToken(TokenType.ENDIF):
                    self.statement()

                self.match(TokenType.ENDIF)

            # "WHILE" comparison "REPEAT" {statement} "ENDWHILE"
            elif self.checkToken(TokenType.WHILE):
                print("STATEMENT-WHILE")
                self.nextToken()
                self.comparison()

                self.match(TokenType.REPEAT)
                self.nl()

                # Zero or more statements in the loop body.
                while not self.checkToken(TokenType.ENDWHILE):
                    self.statement()

                self.match(TokenType.ENDWHILE)
            # "LABEL" ident
            elif self.checkToken(TokenType.LABEL):
                print("STATEMENT-LABEL")
                self.nextToken()
                self.match(TokenType.IDENT)

            # "GOTO" ident
            elif self.checkToken(TokenType.GOTO):
                print("STATEMENT-GOTO")
                self.nextToken()
                self.match(TokenType.IDENT)

            # "LET" ident "=" expression
            elif self.checkToken(TokenType.LET):
                print("STATEMENT-LET")
                self.nextToken()
                self.match(TokenType.IDENT)
                self.match(TokenType.EQ)
                self.expression()

            # "INPUT" ident
            elif self.checkToken(TokenType.INPUT):
                print("STATEMENT-INPUT")
                self.nextToken()
                self.match(TokenType.IDENT)

            # This is not a valid statement. Error!
            else:
                self.abort("Invalid statement at " + self.curToken.text + " (" + self.curToken.kind.name + ")")

            # Newline.
            self.nl()

    # nl ::= '\n'+
    def nl(self):
        print("NEWLINE")
		
        # Require at least one newline.
        self.match(TokenType.NEWLINE)
        # But we will allow extra newlines too, of course.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
