import unittest

from langtools.lexer.token import Token
from tests.lexing_tests.utils import compare_token_list, get_tokens


class ArrayTests(unittest.TestCase):
    def test__tokenize__SimpleArray__Success(self):
        self.assertTrue(
            compare_token_list(
                get_tokens("[1,2,3,4,5]"),
                [
                    Token(name="LEFT_SQUARE", lexme="["),
                    Token(name="NUMBER", lexme="1"),
                    Token(name="COMMA", lexme=","),
                    Token(name="NUMBER", lexme="2"),
                    Token(name="COMMA", lexme=","),
                    Token(name="NUMBER", lexme="3"),
                    Token(name="COMMA", lexme=","),
                    Token(name="NUMBER", lexme="4"),
                    Token(name="COMMA", lexme=","),
                    Token(name="NUMBER", lexme="5"),
                    Token(name="RIGHT_SQUARE", lexme="]"),
                ],
            )
        )

    def test__tokenize__MixedArray__Success(self):
        self.assertTrue(
            compare_token_list(
                get_tokens('[true,"2", -3.5E23,"4e5", false, null]'),
                [
                    Token(name="LEFT_SQUARE", lexme="["),
                    Token(name="TRUE", lexme="true"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"2"'),
                    Token(name="COMMA", lexme=","),
                    Token(name="NUMBER", lexme="-3.5E23"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"4e5"'),
                    Token(name="COMMA", lexme=","),
                    Token(name="FALSE", lexme="false"),
                    Token(name="COMMA", lexme=","),
                    Token(name="NULL", lexme="null"),
                    Token(name="RIGHT_SQUARE", lexme="]"),
                ],
            )
        )

    def test__tokenize__Object__Success(self):
        self.assertTrue(
            compare_token_list(
                get_tokens('{"a": 1, "b": true, "c": null, "-543E23": false}'),
                [
                    Token(name="LEFT_CURLY", lexme="{"),
                    Token(name="STRING", lexme='"a"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="NUMBER", lexme="1"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"b"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="TRUE", lexme="true"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"c"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="NULL", lexme="null"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"-543E23"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="FALSE", lexme="false"),
                    Token(name="RIGHT_CURLY", lexme="}"),
                ],
            )
        )

    def test__tokenize__ObjectsAndArrays__Success(self):
        self.assertTrue(
            compare_token_list(
                get_tokens(
                    """
                    {
                        "a": 1,
                        "b": true,
                        "c": null,
                        "-543E23": false,
                        "f": [true, "2", -3.5e23, "4e5", false, null,
                            { "a": 1,
                                        "b": 2,
                                        "c": 3
                                        }

                        ]
                    }
                """
                ),
                [
                    Token(name="LEFT_CURLY", lexme="{"),
                    Token(name="STRING", lexme='"a"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="NUMBER", lexme="1"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"b"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="TRUE", lexme="true"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"c"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="NULL", lexme="null"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"-543E23"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="FALSE", lexme="false"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"f"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="LEFT_SQUARE", lexme="["),
                    Token(name="TRUE", lexme="true"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"2"'),
                    Token(name="COMMA", lexme=","),
                    Token(name="NUMBER", lexme="-3.5e23"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"4e5"'),
                    Token(name="COMMA", lexme=","),
                    Token(name="FALSE", lexme="false"),
                    Token(name="COMMA", lexme=","),
                    Token(name="NULL", lexme="null"),
                    Token(name="COMMA", lexme=","),
                    Token(name="LEFT_CURLY", lexme="{"),
                    Token(name="STRING", lexme='"a"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="NUMBER", lexme="1"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"b"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="NUMBER", lexme="2"),
                    Token(name="COMMA", lexme=","),
                    Token(name="STRING", lexme='"c"'),
                    Token(name="COLON", lexme=":"),
                    Token(name="NUMBER", lexme="3"),
                    Token(name="RIGHT_CURLY", lexme="}"),
                    Token(name="RIGHT_SQUARE", lexme="]"),
                    Token(name="RIGHT_CURLY", lexme="}"),
                ],
            )
        )
