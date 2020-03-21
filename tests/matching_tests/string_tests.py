import unittest
from src.language_tools_config.lexer_config import LexerConfig

from langtools.lexer.dfa import DFA


class StringTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.string = DFA(LexerConfig.STRING)

    def test__match__EmptyString__Match(self):
        self.assertTrue(self.string.match('""'))

    def test__match__SingleQuote__NoMatch(self):
        self.assertFalse(self.string.match('"'))

    def test__match__HappyPath__Match(self):
        self.assertTrue(self.string.match('"abc"'))
        self.assertTrue(self.string.match('"123"'))
        self.assertTrue(self.string.match('"8978%433!@#$*%&($#&asdfnn~~!133"'))

    def test__match__EscapedQuote__Match(self):
        self.assertTrue(self.string.match('"\\""'))

    def test__match__UnescapedQuote__NoMatch(self):
        self.assertFalse(self.string.match('"""'))

    def test__match__EscapeBackslash__Match(self):
        self.assertFalse(self.string.match('"\\\\""'))

    def test__match__HexNumber__Match(self):
        self.assertTrue(self.string.match('"abc123\\uFFFA3E"'))
        self.assertTrue(self.string.match('"\\uABCDEF"'))
        self.assertTrue(self.string.match('"\\uabcdef"'))
        self.assertTrue(self.string.match('"\\u123456"'))

    def test__match__Newline__Match(self):
        self.assertTrue(self.string.match('"\\n"'))
        self.assertTrue(self.string.match('"abc123\\nabc123"'))

    def test__match__MoreEscapeCharacters__Match(self):
        self.assertTrue(self.string.match('"\\\\"'))
        self.assertTrue(self.string.match('"\\/"'))
        self.assertTrue(self.string.match('"\\b"'))
        self.assertTrue(self.string.match('"\\f"'))
        self.assertTrue(self.string.match('"\\r"'))
        self.assertTrue(self.string.match('"\\t"'))

    def test__match__MissingCloseQuote__NoMatch(self):
        self.assertFalse(self.string.match('"asdbf234fjadf'))
