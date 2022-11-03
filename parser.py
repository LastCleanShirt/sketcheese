# TODO: PARSER
from token import *
from errorcall import *

class Parser:
    def __init__(self, lex):
        self.text = lex
        self.token = []
        self.variables = None
        self.functions = None

    def parse(self):
        #print(str(self.text))
        toks = []
        variables = {}
        functions = {}

        for x in range(len(self.text)):
        #    if self.text[x][0] == K_OUT and self.text[x+1][0] == K_STR:
                #print(f'{self.text[x+1][1]}'.replace("\\", ""))
                #toks.append(Token(K_OUT, self.text[x+1][1]))

            #elif self.text[x][0] == K_OUT and self.text[x+1][0] == TT_VAR_CALL:
                #print(variables[self.text[x+1][1]])
                #variables.append([f"{self.text[x+1][1]}" : f"{self.text[x+3][1]}"])
            if self.text[x][0] == TT_DECLR:
                if self.text[x+1][0] == TT_DECLR_NAME:
                    if self.text[x+2][0] == TT_EQ:
                        if self.text[x+3][0] == TT_INT:
                            variables[self.text[x+1][1]] = int(self.text[x+3][1])
                        elif self.text[x+3][0] == TT_FLOAT:
                            variables[self.text[x+1][1]] = float(self.text[x+3][1])
                        elif self.text[x+3][0] == K_STR:
                            variables[self.text[x+1][1]] = str(self.text[x+3][1])
                        else:
                            print("The value of the variable '"+self.text[x+1][1]+"' is not recognized as either integer, string or float")
                    else:
                        print("Needs eq")
                else:
                    print(IllegalCharError("WOW"))
                    print("Needs a proper variable name dumbass")

            elif self.text[x][0] == K_FUNC:
                if self.text[x+1][0] == TT_FUNC_N:
                    if self.text[x+2][0] == TT_LPAREN and self.text[x+3][0] == TT_RPAREN:
                        functions[self.text[x+1][1]] = "function content"

            else:
                pass

        self.toks = toks
        self.variables = variables#print(variables)
        self.functions = functions
