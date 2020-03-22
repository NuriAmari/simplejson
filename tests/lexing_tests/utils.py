from typing import List

from langtools.lexer.token import Token
from langtools.lexer.lexer import tokenize_str

from src.language_tools_config.lexer_config import LexerConfig


def get_tokens(input_str: str):
    return tokenize_str(input_str, LexerConfig.TOKENIZER)


def compare_token_list(list1: List[Token], list2: List[Token]) -> bool:

    # TODO Improve mismatch diff
    if len(list1) != len(list2):
        print(f"No Match: Differing number of tokens: {len(list1)} != {len(list2)}")
        return False

    index = 0
    for token1, token2 in zip(list1, list2):
        if token1.lexme != token2.lexme:
            print(f"Mismatch at index: {index}:", token1, token2)
            return False

        index += 1

    return True
