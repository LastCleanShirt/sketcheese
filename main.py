# Import the system library to get arguments
import sys
import re
import argparse
import datetime
from lexer import Lexer
from parser import Parser
from errorcall import Error
from compiletopy import Compiler


class Main:
    # Initionalization
    def __init__(self, args):
        self.execTime = datetime.datetime.now()
        self.args = args
        self.file = None;
        self.err = Error()
        self.parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="A Programming Language made for fun.",
        epilog="Note that this program is still on heavy development."
        )
        self.parser.add_argument("filepath", type=str)
        self.parser.add_argument("-i", default=True)
        self.parser.add_argument("-ctpy", default=False)
        self.parser.add_argument("-log", default=False)

        self.arg_p = self.parser.parse_args()
        self.file_path = self.arg_p.filepath;
        self.is_log = self.arg_p.log

        self.chars = None;

        self.RESERVED = "RESERVED"
        self.INT = "INT"
        self.ID = "ID"

        self.toks = None;
        self.pos = None;
        self.vars = None;
        self.funcs = None;

        self.token_exprs = [
        (r"[ \n\t]+", None),
        (r"\=", self.RESERVED),
        (r"decl", self.RESERVED),
        (r"\"", self.RESERVED),
        (r"\'", self.RESERVED),
        (r"[A-Za-z][A-Za-z0-9_]*", self.ID)
        ]

    # Cmd Line
    def CmdLine(self):
        try:
            #self.file_path = self.args[1]
            print(self.file_path)
            self.file = open(self.file_path, "r")
            self.chars = self.file.read()
            if self.arg_p.i:
                self.Lexer(self.chars, self.token_exprs)
                self.Parser()
            elif self.arg_p.ctpy:
                self.Lexer(self.chars, self.token_exprs)
            else:
                pass

            if self.is_log:
                self.PrintLog()
        except IndexError as e:
            print(e)
            self.err.PrintErr(0, "Please specify the filename")
    # Lexing
    def Lexer(self, characters, token_exprs):
        lexer = Lexer(characters)
        tokens, error = lexer.make_tokens()
        self.toks = tokens
        #print(tokens)

    # Parsing
    def Parser(self):
        parser = Parser(self.toks)
        parser.parse()
        self.vars = parser.variables
        self.funcs = parser.functions

    # Logs
    def PrintLog(self):
        print(f"\nLog from {self.file_path} at {self.execTime}")
        print(f"\tTokens:\n{self.toks}\n")
        print(f"\tVariables:\n{self.vars}")
        print(f"\tFunctions:\n{self.funcs}")

if __name__ == "__main__":
    main = Main(sys.argv)
    main.CmdLine()
    #main.PrintLog()
    #main.Lexer(main.chars, main.token_exprs)
    #main.Parser(main.toks)
    #main.Interp()
