import json as simplejson

from typing import TextIO

from languagetools.ast.ast import ASTNode


class json:
    @staticmethod
    def loads(input_str: str) -> object:
        pass

    @staticmethod
    def load(input_str: str) -> object:
        pass

    @staticmethod
    def dumps(json_object: object) -> str:
        pass

    @staticmethod
    def dump(json_object: object, stream: TextIO) -> None:
        pass

    @staticmethod
    def ast_to_object(ast: ASTNode) -> object:
        if ast.name == "VALUE":
            return json.ast_to_object(ast.children[0])
        elif ast.name == "STRING":
            if ast.lexme is None:
                raise Exception("Terminals should always have a non null lexme")
            return ast.lexme[1 : len(ast.lexme) - 1]
        elif ast.name == "TRUE":
            return True
        elif ast.name == "FALSE":
            return False
        elif ast.name == "NULL":
            return None
        elif ast.name == "NUMBER":
            # TODO Handle decoding hex, exponents, floats
            if ast.lexme is None:
                raise Exception("Terminals should always have a non null lexme")
            return simplejson.loads(ast.lexme)
        elif ast.name == "ARRAY":
            result = []
            for child in ast.children[1].children:
                if child.name == "ELEMENT":
                    result.append(json.ast_to_object(child))
            return result
        elif ast.name == "ELEMENT":
            return json.ast_to_object(ast.children[0])
        elif ast.name == "OBJECT":
            result = {}
            for child in ast.children[1].children:
                if child.name == "MEMBER":
                    result[
                        child.children[0].lexme[1 : len(child.children[0].lexme) - 1]
                    ] = json.ast_to_object(child.children[2])
            return result
        elif ast.name == "S-Prime":
            return json.ast_to_object(ast.children[1])
        elif ast.name == "JSON":
            return json.ast_to_object(ast.children[0])
