import unittest

from langtools.lexer.nfa import Union
from langtools.lexer.dfa import DFA

from src.language_tools_config.lexer_config import LexerConfig


class PunctuationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.punctuation = DFA(
            Union(
                LexerConfig.COLON,
                LexerConfig.COMMA,
                LexerConfig.LEFT_CURLY,
                LexerConfig.RIGHT_CURLY,
                LexerConfig.LEFT_SQUARE,
                LexerConfig.RIGHT_SQUARE,
                LexerConfig.TRUE,
                LexerConfig.FALSE,
                LexerConfig.NULL,
            )
        )

    def test__match__Brackets__Match(self):
        self.assertTrue(self.punctuation.match("{"))
        self.assertTrue(self.punctuation.match("}"))
        self.assertTrue(self.punctuation.match("["))
        self.assertTrue(self.punctuation.match("]"))

    def test__match__Seperators__Match(self):
        self.assertTrue(self.punctuation.match(":"))
        self.assertTrue(self.punctuation.match(","))

    def test__match__Keywords__Match(self):
        self.assertTrue(self.punctuation.match("true"))
        self.assertTrue(self.punctuation.match("false"))
        self.assertTrue(self.punctuation.match("null"))
