# TODO: tokens

# LIST OF CONSTANTS
DIGITS = "0123456789"
WORDS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
K_OUT = "<out keyword>" # Prints out string or variable
K_STR = "<string>"
K_FUNC = "<function declr>"
TT_FUNC_N = "<function name>"
TT_ST = "<start func define>" # The start of the function
TT_END = "<end func define>" # The end of the function
TT_DECLR = "<var declr>" # $
TT_DECLR_NAME = "<var name>"
TT_VAR_CALL = "<var call>"
NK = "<not keyword>"

# LIST OF TOKENS
TT_INT = '<int obj>'
TT_FLOAT = '<float obj>'
TT_PLUS = '<plus tk>'
TT_MINUS = '<min tk>'
TT_DIV = '<div tk>'
TT_LPAREN = '<lparen tk>' # (
TT_RPAREN = '<rparen tk>' # )
TT_LAPOS = "<lapos tk>" # Left Apostrophe
TT_RAPOS = "<rapos tk>" # Right Apostrophe
TT_EQ = "<eq tk>"


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
