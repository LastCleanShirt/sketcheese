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
        temp_declr = ''
        temp_kw = ''
        state = 0
        declr_state = 0

        while self.current_char != None:
            print(temp)
            print(tokens)
            print(state)
            # Skip a few characters
            if self.current_char in '\n\t ' and state == 0:
                self.advance()
                #tokens.append(Token(NK, temp_kw))
                temp = ''
                temp_kw = ''
                #temp_declr = ''
                #self.line += 1
                # Detect strings and stuff


            elif self.current_char == "\"":
                print("found this shhit")
                if state == 0:
                    state = 1
                    self.advance()
                elif state == 1:
                    tokens.append(Token(K_STR, temp))
                    temp = ''
                    state = 0
                    self.advance()

            elif self.current_char == "\'":
                if state == 0:
                    state = 1
                    self.advance()
                elif state == 1:
                    tokens.append(Token(K_STR, temp))
                    temp = ''
                    temp_str = ""
                    state = 0
                    self.advance()

            elif state == 1:
                temp += self.current_char
                self.advance()

            elif self.current_char in WORDS:
                # Check if the current character that is scanned is not inside of a string
                temp_kw += self.current_char
                print(temp_kw)
                if declr_state == 1:
                    temp_declr += self.current_char
                elif state == 1:
                    temp += self.current_char
                # Detect the "out"
                elif temp_kw == "out":
                    tokens.append(Token(K_OUT, " "))
                    temp_kw = ''
                else:
                    pass


                self.advance()

            # TODO: Digits
            elif self.current_char in DIGITS:
                if state == 0:
                    tokens.append(self.make_number())
                    self.advance()
                else:
                    temp += self.current_char
                    self.advance()

            # PLUS TOKEN
            elif self.current_char == '+' :
                tokens.append(Token(TT_PLUS, "+"))
                #print("TT_PLUS")
                self.advance()
            # MINUS TOKEN
            elif self.current_char == '-' :
                #temp += self.current_char
                tokens.append(Token(TT_MINUS, "-"))
                self.advance()
            # MULTIPLY TOKEN
            elif self.current_char == "*" :
                tokens.append(Token(TT_MUL, "*"))
                self.advance()
            # DIVIDE TOKEN
            elif self.current_char == "/" :
                tokens.append(Token(TT_DIV, "/"))
                self.advance()
            # LPARANTESES
            elif self.current_char == "(" :
                tokens.append(Token(TT_LPAREN, "("))
                #temp = ""
                #print("LPAREN")
                self.advance()
            # RPARANTESES
            elif self.current_char == ")" :
                tokens.append(Token(TT_RPAREN, ")"))
                self.advance()
            # DECLR
            elif self.current_char == "$" :
                tokens.append(Token(TT_DECLR, "$"))
                declr_state = 1
                self.advance()
            # VARIABLE_CALL
            elif self.current_char == "!" :
                tokens.append(Token(TT_VAR_CALL, temp))
                temp = ''
                self.advance()
            # START
            elif self.current_char == ":" :
                tokens.append(Token(TT_ST, "FUNC_START"))
                temp = ''
                self.advance()
            # EQ
            elif self.current_char == "=" :
                tokens.append(Token(TT_DECLR_NAME, temp_declr))
                tokens.append(Token(TT_EQ, "="))
                declr_state = 0
                temp_declr = ""

                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "''")

            """print("POS: "+str(self.pos))
            print("temp: "+temp_str)
            print("Current char: "+str(self.current_char))
            print("State: "+str(state))
            """
        print(tokens)

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
            if num_str == '0': return Token(TT_INT, "0")
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))
