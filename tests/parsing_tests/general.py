import unittest

from typing import List

from langtools.lexer.token import Token

from src.language_tools_config.parser_config import ParserConfig


def parse(tokens: List[Token]):
    return ParserConfig.JSON_GRAMMAR.LL1_parse(tokens)


class SingleLiteralTests(unittest.TestCase):
    def test__LL1_parse__True__Success(self):
        try:
            parse([Token(name="TRUE")])
        except:
            self.fail("Exception raised while parsing true")

    def test__LL1_parse__False__Success(self):
        try:
            parse([Token(name="FALSE")])
        except:
            self.fail("Exception raised while parsing false")

    def test__LL1_parse__Null__Success(self):
        try:
            parse([Token(name="NULL")])
        except:
            self.fail("Exception raised while parsing null")

    def test__LL1_parse__Number__Success(self):
        try:
            parse([Token(name="NUMBER")])
        except:
            self.fail("Exception raised while parsing number")

    def test__LL1_parse__String__Success(self):
        try:
            parse([Token(name="STRING")])
        except:
            self.fail("Exception raised while parsing string")

    def test__LL1_parse__Object__Success(self):
        try:
            parse([Token(name="LEFT_CURLY"), Token(name="RIGHT_CURLY")])
        except:
            self.fail("Exception raised while parsing object")

    def test__LL1_parse__Array__Success(self):
        try:
            parse([Token(name="LEFT_SQUARE"), Token(name="RIGHT_SQUARE")])
        except:
            self.fail("Exception raised while parsing square")


class SimpleJsonTests(unittest.TestCase):
    def test__LL1_parse__Array__Success(self):
        try:
            parse(
                [
                    Token(name="LEFT_SQUARE"),
                    Token(name="NUMBER"),
                    Token(name="COMMA"),
                    Token(name="NUMBER"),
                    Token(name="RIGHT_SQUARE"),
                ]
            )
        except:
            self.fail("Exception raised while parsing array")

    def test__LL1_parse__Object__Success(self):
        try:
            parse(
                [
                    Token(name="LEFT_CURLY"),
                    Token(name="STRING"),
                    Token(name="COLON"),
                    Token(name="NUMBER"),
                    Token(name="COMMA"),
                    Token(name="STRING"),
                    Token(name="COLON"),
                    Token(name="NUMBER"),
                    Token(name="RIGHT_CURLY"),
                ]
            )
        except:
            self.fail("Exception raised while parsing object")
