import unittest

from src.language_tools_config.lexer_config import LexerConfig
from langtools.lexer.dfa import DFA


class NumberTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.number = DFA(LexerConfig.NUMBER)

    def test__match__SingleDigit__Match(self):
        self.assertTrue(self.number.match("0"))
        self.assertTrue(self.number.match("1"))
        self.assertTrue(self.number.match("2"))
        self.assertTrue(self.number.match("3"))
        self.assertTrue(self.number.match("4"))
        self.assertTrue(self.number.match("5"))
        self.assertTrue(self.number.match("6"))
        self.assertTrue(self.number.match("7"))
        self.assertTrue(self.number.match("8"))
        self.assertTrue(self.number.match("9"))

    def test__match__SingleNegativeDigit__Match(self):
        self.assertTrue(self.number.match("-0"))
        self.assertTrue(self.number.match("-1"))
        self.assertTrue(self.number.match("-2"))
        self.assertTrue(self.number.match("-3"))
        self.assertTrue(self.number.match("-4"))
        self.assertTrue(self.number.match("-5"))
        self.assertTrue(self.number.match("-6"))
        self.assertTrue(self.number.match("-7"))
        self.assertTrue(self.number.match("-8"))
        self.assertTrue(self.number.match("-9"))

    def test__match__MultiDigit__Match(self):
        self.assertTrue(self.number.match("123"))
        self.assertTrue(self.number.match("234"))
        self.assertTrue(self.number.match("345"))
        self.assertTrue(self.number.match("456"))
        self.assertTrue(self.number.match("567"))
        self.assertTrue(self.number.match("678"))
        self.assertTrue(self.number.match("789"))
        self.assertTrue(self.number.match("890"))
        self.assertTrue(self.number.match("901"))

    def test__match__MultiNegativeDigit__Match(self):
        self.assertTrue(self.number.match("-123"))
        self.assertTrue(self.number.match("-234"))
        self.assertTrue(self.number.match("-345"))
        self.assertTrue(self.number.match("-456"))
        self.assertTrue(self.number.match("-567"))
        self.assertTrue(self.number.match("-678"))
        self.assertTrue(self.number.match("-789"))
        self.assertTrue(self.number.match("-890"))
        self.assertTrue(self.number.match("-901"))

    def test_match__ZeroPaddedMultiDigit__NoMatch(self):
        self.assertFalse(self.number.match("0123"))
        self.assertFalse(self.number.match("0234"))
        self.assertFalse(self.number.match("0345"))
        self.assertFalse(self.number.match("0456"))
        self.assertFalse(self.number.match("0567"))
        self.assertFalse(self.number.match("0678"))
        self.assertFalse(self.number.match("0789"))
        self.assertFalse(self.number.match("0890"))
        self.assertFalse(self.number.match("0901"))
        self.assertFalse(self.number.match("-0123"))
        self.assertFalse(self.number.match("-0234"))
        self.assertFalse(self.number.match("-0345"))
        self.assertFalse(self.number.match("-0456"))
        self.assertFalse(self.number.match("-0567"))
        self.assertFalse(self.number.match("-0678"))
        self.assertFalse(self.number.match("-0789"))
        self.assertFalse(self.number.match("-0890"))
        self.assertFalse(self.number.match("-0901"))

    def test__match__Float__Match(self):
        self.assertTrue(self.number.match("123.123"))
        self.assertTrue(self.number.match("234.234"))
        self.assertTrue(self.number.match("345.345"))
        self.assertTrue(self.number.match("456.456"))
        self.assertTrue(self.number.match("567.567"))
        self.assertTrue(self.number.match("678.678"))
        self.assertTrue(self.number.match("789.789"))
        self.assertTrue(self.number.match("890.890"))
        self.assertTrue(self.number.match("901.901"))
        self.assertTrue(self.number.match("-123.123"))
        self.assertTrue(self.number.match("-234.234"))
        self.assertTrue(self.number.match("-345.345"))
        self.assertTrue(self.number.match("-456.456"))
        self.assertTrue(self.number.match("-567.567"))
        self.assertTrue(self.number.match("-678.678"))
        self.assertTrue(self.number.match("-789.789"))
        self.assertTrue(self.number.match("-890.890"))
        self.assertTrue(self.number.match("-901.901"))

    def test__match__ZeroPaddedFloat__NoMatch(self):
        self.assertFalse(self.number.match("0123.123"))
        self.assertFalse(self.number.match("0234.234"))
        self.assertFalse(self.number.match("0345.345"))
        self.assertFalse(self.number.match("0456.456"))
        self.assertFalse(self.number.match("0567.567"))
        self.assertFalse(self.number.match("0678.678"))
        self.assertFalse(self.number.match("0789.789"))
        self.assertFalse(self.number.match("0890.890"))
        self.assertFalse(self.number.match("0901.901"))
        self.assertFalse(self.number.match("-0123.123"))
        self.assertFalse(self.number.match("-0234.234"))
        self.assertFalse(self.number.match("-0345.345"))
        self.assertFalse(self.number.match("-0456.456"))
        self.assertFalse(self.number.match("-0567.567"))
        self.assertFalse(self.number.match("-0678.678"))
        self.assertFalse(self.number.match("-0789.789"))
        self.assertFalse(self.number.match("-0890.890"))
        self.assertFalse(self.number.match("-0901.901"))

    def test__match__Exponent__Match(self):
        self.assertTrue(self.number.match("5e34"))
        self.assertTrue(self.number.match("5e023"))
        self.assertTrue(self.number.match("5e-34"))
        self.assertTrue(self.number.match("5e-034"))
        self.assertTrue(self.number.match("5e+034"))
        self.assertTrue(self.number.match("5.0234e34"))
        self.assertTrue(self.number.match("5.0234e-34"))
        self.assertTrue(self.number.match("5E34"))
        self.assertTrue(self.number.match("5E023"))
        self.assertTrue(self.number.match("5E-34"))
        self.assertTrue(self.number.match("5E-034"))
        self.assertTrue(self.number.match("5E+034"))
        self.assertTrue(self.number.match("5.0234E34"))
        self.assertTrue(self.number.match("5.0234E-34"))

    def test__match__Mismatch__UnsuccesfulMatch(self):

        self.assertFalse(self.number.match(""))
        self.assertFalse(self.number.match("02"))
        self.assertFalse(self.number.match("012"))
        self.assertFalse(self.number.match("012e5"))
        self.assertFalse(self.number.match("a12"))
        self.assertFalse(self.number.match("1A2"))
        self.assertFalse(self.number.match("abc"))
