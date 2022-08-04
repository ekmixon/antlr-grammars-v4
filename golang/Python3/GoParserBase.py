from antlr4 import *

class GoParserBase(Parser):

    def closingBracket(self) -> bool:
        la = self._input.LA(1)
        return la in [self.R_PAREN, self.R_CURLY]
