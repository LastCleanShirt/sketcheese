# TODO: Lexer
from token import Token
from token import *
from errorcall import *

class Lexer:
    # Initionalization
    def __init__(self, characters):
        self.text = characters
        self.toks = None
        self.pos = -1
        self.line = 1
        self.current_char = None
        self.advance()

    # Advance/go to next char
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    # Make tokens
    def make_tokens(self):
        tokens = []
        temp = ''
        temp_str = ''
        state = 0
        declr_state = 0
        temp_declr = ''

        while self.current_char != None:
            # Skip a few characters
            if self.current_char in '\n\t ' and state == 0:
                self.advance()
                self.line += 1
            # Detect strings and stuff
            elif self.current_char == "\"":
                if state == 0:
                    state = 1
                elif state == 1:
                    tokens.append(Token("STR", temp_str))
                    temp_str = ""
                    state = 0
                self.advance()

            elif self.current_char == "\'":
                if state == 0:
                    state = 1
                elif state == 1:
                    tokens.append(Token("STR", f'{temp_str}'))
                    temp_str = ""
                    state = 0
                self.advance()

            elif state == 1:
                temp_str += self.current_char
                #print(self.current_char)
                ##print("temp_str: "+temp_str)
                self.advance()

            # TODO: Digits
            elif self.current_char in DIGITS:
                if state == 0:
                    tokens.append(self.make_number())
                    self.advance()
                else:
                    self.advance()

            elif declr_state == 1:
                #print("declr_state 1")
                if self.current_char == "=":
                    tokens.append(Token(TT_DECLR_NAME, temp_declr))
                    tokens.append(Token(TT_EQ, "="))
                    declr_state = 0
                    temp_declr = ""
                    self.advance()
                elif self.current_char in "(":
                    declr_state = 0
                    self.advance()
                    tokens.append(Token(TT_FUNC_N, temp_declr))
                    tokens.append(Token(TT_LPAREN, "("))
                    temp_declr = ''
                else:
                    temp_declr += self.current_char
                    self.advance()

            # Detecting  keywords and variables
            elif self.current_char in WORDS:
                # Check if the current character that is scanned is not inside of a string
                if state == 0 and declr_state == 0:
                    temp += self.current_char
                    #
                    # The "decl" keyword
                    # Declares Variables & stuff
                    #
                    # The "out" keyword
                    # Prints out strings
                    # For now, the backlash is not working
                    if temp == "out":
                        temp = ''
                        tokens.append(Token(K_OUT, "OUT"))
                        self.advance()
                    # Function Declaration
                    elif temp == "defunc":
                        declr_state = 1
                        temp = ''
                        tokens.append(Token(K_FUNC, "FUNC_DECLR"))
                        self.advance()
                    # Function ends.
                    elif temp == "endf":
                        tokens.append(Token(TT_END, "FUNC_END"))
                        temp = ''
                        self.advance()

                    self.advance()

                elif state == 1: # Skip detection if its inside of a string
                    self.advance()
                elif declr_state == 1:
                    temp_declr += self.current_char
                    self.advance()
                #elif declr_state == 1: # Variable Declaration
                    #print("declr state " + str(declr_state))
                    #print(temp_declr)
                    #print(declr_state)


            # PLUS TOKEN
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, "+"))
                #print("TT_PLUS")
                self.advance()
            # MINUS TOKEN
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, "-"))
                self.advance()
            # MULTIPLY TOKEN
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL, "*"))
                self.advance()
            # DIVIDE TOKEN
            elif self.current_char == "/":
                tokens.append(Token(TT_DIV, "/"))
                self.advance()
            # LPARANTESES
            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN, "("))
                temp = ""
                #print("LPAREN")
                self.advance()
            # RPARANTESES
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN, ")"))
                temp = ""
                self.advance()
            # DECLR
            elif self.current_char == "$":
                tokens.append(Token(TT_DECLR, "$"))
                declr_state = 1
                self.advance()
            # VARIABLE_CALL
            elif self.current_char == "!":
                tokens.append(Token(TT_VAR_CALL, temp))
                temp = ''
                self.advance()
            # START
            elif self.current_char == ":":
                tokens.append(Token(TT_ST, "FUNC_START"))
                temp = ''
                self.advance()
            # EQ
            elif self.current_char == "=":
                if declr_state == 1:
                    #tokens.append(Token(TT_DECLR_NAME, temp_declr))
                    tokens.append(Token(TT_EQ, "="))
                    temp_declr = ''
                    declr_state = 0
                    self.advance()
                elif declr_state == 0:
                    IllegalCharError("TITITLO BAU TAI")
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "''")

            """print("POS: "+str(self.pos))
            print("temp: "+temp_str)
            print("Current char: "+str(self.current_char))
            print("State: "+str(state))
            """
        #print(tokens)

        return tokens, "Err"

    # NUMBERS
    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char == ".":
                if dot_count == 1: break
                dot_count += 1
                num_str += "."
                self.advance()
            else:
                num_str += self.current_char
                self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))
