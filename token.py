# TODO: tokens

# LIST OF CONSTANTS
DIGITS = "0123456789"
WORDS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
K_OUT = "OUT" # Prints out string or variable
K_STR = "STR"
K_FUNC = "DECLR_FUNC"
TT_FUNC_N = "FUNC_N"
TT_ST = "START" # The start of the function
TT_END = "END" # The end of the function
TT_DECLR = "DECLR" # $
TT_DECLR_NAME = "DECLR_NAME"
TT_VAR_CALL = "VAR_CALL"


# LIST OF TOKENS
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN' # (
TT_RPAREN = 'RPAREN' # )
TT_LAPOS = "LAPOS" # Left Apostrophe
TT_RAPOS = "RAPOS" # Right Apostrophe
TT_EQ = "EQ"


"""class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return "[{}, {}]".format(self.type, ", ".join(self.value))#return f'{self.type}:{self.value
         #f'{self.type}'
"""

def Token(type, value):
    if value: return [type, value]
    return type
