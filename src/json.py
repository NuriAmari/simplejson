import json as simplejson
import io
import re

from typing import TextIO, Union

from langtools.ast.ast import ASTNode
from langtools.lexer.lexer import tokenize
from src.language_tools_config.parser_config import ParserConfig
from src.language_tools_config.lexer_config import LexerConfig


def parse_number(number_str: str) -> Union[int, float]:

    # maybe using re is slightly cheating, but I'm ok with it
    groups = re.match(
        r"([+-]?[0-9]+)(\.[0-9]+)?([eE][+-]?[0-9]+)?", number_str
    ).groups()

    integer_component = int(groups[0])
    decimal_component = float(f"0.{groups[1][1:]}") if groups[1] else 0
    exponent_component = int(groups[2][1:]) if groups[2] else 0

    if integer_component < 0:
        decimal_component *= -1

    return (integer_component + decimal_component) * 10 ** exponent_component


class json:
    @staticmethod
    def loads(input_str: str) -> object:
        tokens = tokenize(io.StringIO(input_str), LexerConfig.TOKENIZER)
        tree = ParserConfig.JSON_GRAMMAR.LL1_parse(tokens)
        tree.flatten({"ELEMENTS": "ANOTHER_ELEMENT", "MEMBERS": "ANOTHER_MEMBER"})
        return json.ast_to_object(tree)

    @staticmethod
    def load(input_stream: str) -> object:
        tokens = tokenize(input_stream, LexerConfig.TOKENIZER)
        tree = ParserConfig.JSON_GRAMMAR.LL1_parse(tokens)
        tree.flatten({"ELEMENTS": "ANOTHER_ELEMENT", "MEMBERS": "ANOTHER_MEMBER"})
        return json.ast_to_object(tree)

    @staticmethod
    def dumps(json_object: object) -> str:
        return simplejson.dumps(json_object)

    @staticmethod
    def dump(json_object: object, stream: TextIO) -> None:
        simplejson.dump(json_object, stream)

    @staticmethod
    def ast_to_object(ast: ASTNode) -> object:
        retval = None

        if ast.name == "VALUE":
            retval = json.ast_to_object(ast.children[0])
        elif ast.name == "STRING":
            if ast.lexme is None:
                raise Exception("Terminals should always have a non null lexme")
            retval = ast.lexme[1 : len(ast.lexme) - 1]
        elif ast.name == "TRUE":
            retval = True
        elif ast.name == "FALSE":
            retval = False
        elif ast.name == "NULL":
            retval = None
        elif ast.name == "NUMBER":
            if ast.lexme is None:
                raise Exception("Terminals should always have a non null lexme")
            retval = parse_number(ast.lexme)
        elif ast.name == "ARRAY":
            result = []
            for child in ast.children[1].children:
                if child.name == "ELEMENT":
                    result.append(json.ast_to_object(child))
            retval = result
        elif ast.name == "ELEMENT":
            retval = json.ast_to_object(ast.children[0])
        elif ast.name == "OBJECT":
            result = {}
            for child in ast.children[1].children:
                if child.name == "MEMBER":
                    result[
                        child.children[0].lexme[1 : len(child.children[0].lexme) - 1]
                    ] = json.ast_to_object(child.children[2])
            retval = result
        elif ast.name == "S-Prime":
            retval = json.ast_to_object(ast.children[1])
        elif ast.name == "JSON":
            retval = json.ast_to_object(ast.children[0])
        else:
            raise Exception(f"Failed to convert ast node with name {ast.name}")

        return retval
