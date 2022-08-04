from antlr4 import *

class PlSqlLexerBase(Lexer):

    def IsNewlineAtPos(self, pos):
        la = self._input.LA(pos)
        return la in [-1, 10] 
