import unittest
from typing import List

from langtools.lexer.lexer import tokenize_str
from langtools.lexer.token import Token
from langtools.lexer.exceptions import LexicalError

from src.language_tools_config.lexer_config import LexerConfig


def compare_token_list(list1: List[Token], list2: List[Token]) -> bool:

    if len(list1) != len(list2):
        print("No Match:", list1, list2)
        return False

    for token1, token2 in zip(list1, list2):
        if token1.lexme != token2.lexme:
            print("No Match:", list1, list2)
            return False

    return True


def get_tokens(input_str: str):
    return tokenize_str(input_str, LexerConfig.TOKENIZER)


class SingleToken(unittest.TestCase):
    def test__tokenize__Numbers__Success(self):
        self.assertTrue(
            compare_token_list(get_tokens("1"), [Token(name="NUMBER", lexme="1")])
        )

        self.assertTrue(
            compare_token_list(
                get_tokens("12345"), [Token(name="NUMBER", lexme="12345")]
            )
        )

        self.assertTrue(
            compare_token_list(
                get_tokens("1.05234E-23"), [Token(name="NUMBER", lexme="1.05234E-23")]
            )
        )

        self.assertTrue(
            compare_token_list(
                get_tokens("-1.05234E-23"),
                [Token(name="NUMBER", lexme="-1.05234E-23")],
            )
        )

        self.assertTrue(
            compare_token_list(get_tokens("0"), [Token(name="NUMBER", lexme="0")])
        )

    def test__tokenize_Numbers__Failure(self):
        with self.assertRaises(LexicalError) as context:
            get_tokens("01")

        self.assertEqual("1", context.exception.error_char)
        self.assertEqual(0, context.exception.error_line)
        self.assertEqual(1, context.exception.error_col)
