import unittest

from langtools.lexer.token import Token
from langtools.lexer.exceptions import LexicalError

from tests.lexing_tests.utils import compare_token_list, get_tokens


class NumberTests(unittest.TestCase):
    def test__tokenize__SingleDigit__Success(self):
        self.assertTrue(
            compare_token_list(get_tokens("1"), [Token(name="NUMBER", lexme="1")])
        )

    def test__tokenize__MultiDigit__Success(self):
        self.assertTrue(
            compare_token_list(
                get_tokens("12345"), [Token(name="NUMBER", lexme="12345")]
            )
        )

    def test__tokenize__FancyNumbers__Success(self):

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

    def test__tokenize_Zero__Success(self):

        self.assertTrue(
            compare_token_list(get_tokens("0"), [Token(name="NUMBER", lexme="0")])
        )

    def test__tokenize_ZeroNonZero__TwoSeperateTokens(self):
        self.assertTrue(
            compare_token_list(
                get_tokens("01"),
                [Token(name="NUMBER", lexme="0"), Token(name="NUMBER", lexme="1")],
            )
        )

    def test__tokenize_SecondDecimalPoint__Failure(self):

        with self.assertRaises(LexicalError) as context:
            tokens = get_tokens("1.5.5")
            print(tokens)

        self.assertEqual(".", context.exception.error_char)
        self.assertEqual(0, context.exception.error_line)
        self.assertEqual(3, context.exception.error_col)

    def test__tokenize_SecondExponent__Failure(self):

        with self.assertRaises(LexicalError) as context:
            tokens = get_tokens("1.5e\n5e6")
            print(tokens)

        self.assertEqual("e", context.exception.error_char)
        self.assertEqual(1, context.exception.error_line)
        self.assertEqual(1, context.exception.error_col)


class StringTests(unittest.TestCase):
    def test__tokenize__SingleString__Success(self):
        self.assertTrue(
            compare_token_list(get_tokens('""'), [Token(name="STRING", lexme='""')])
        )

    def test__tokenize__FancyString__Success(self):
        self.assertTrue(
            compare_token_list(
                get_tokens('"\\"\\nabc123#$%$#"'),
                [Token(name="STRING", lexme='"\\"\\nabc123#$%$#"')],
            )
        )
