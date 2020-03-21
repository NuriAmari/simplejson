import unittest

from src.language_tools_config.parser_config import ParserConfig


class GrammarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.json_grammar = ParserConfig.JSON_GRAMMAR

    def test__is_grammar_LL1__HappyPath__Yes(self):

        self.assertTrue(self.json_grammar.is_grammar_LL1())
