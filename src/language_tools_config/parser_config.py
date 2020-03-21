from langtools.parser.cfg import CFG, Terminal, NonTerminal, ProductionRule
from langtools.parser.cfg import Epsilon


class ParserConfig:

    # NON_TERMINALS

    JSON = NonTerminal(name="JSON")
    ELEMENT = NonTerminal(name="ELEMENT")
    ANOTHER_ELEMENT = NonTerminal(name="ANOTHER_ELEMENT")
    VALUE = NonTerminal(name="VALUE")
    OBJECT = NonTerminal(name="OBJECT")
    ARRAY = NonTerminal(name="ARRAY")
    VALUE = NonTerminal(name="VALUE")
    VALUE = NonTerminal(name="VALUE")
    VALUE = NonTerminal(name="VALUE")
    MEMBERS = NonTerminal(name="MEMBERS")
    MEMBER = NonTerminal(name="MEMBER")
    ANOTHER_MEMBER = NonTerminal(name="ANOTHER_MEMBER")
    ELEMENTS = NonTerminal(name="ELEMENTS")

    # TERMINALS

    true = Terminal(name="TRUE")
    false = Terminal(name="FALSE")
    null = Terminal(name="NULL")
    string = Terminal(name="STRING")
    number = Terminal(name="NUMBER")
    comma = Terminal(name="COMMA")
    colon = Terminal(name="COLON")
    left_curly = Terminal(name="LEFT_CURLY")
    left_square = Terminal(name="LEFT_SQUARE")
    right_curly = Terminal(name="RIGHT_CURLY")
    right_square = Terminal(name="RIGHT_SQUARE")

    # PRODUCTION RULES

    PRODUCTION_RULES = [
        ProductionRule(JSON, [VALUE]),
        ProductionRule(VALUE, [OBJECT]),
        ProductionRule(VALUE, [ARRAY]),
        ProductionRule(VALUE, [string]),
        ProductionRule(VALUE, [number]),
        ProductionRule(VALUE, [true]),
        ProductionRule(VALUE, [false]),
        ProductionRule(VALUE, [null]),
        ProductionRule(OBJECT, [left_curly, MEMBERS, right_curly]),
        ProductionRule(MEMBERS, [Epsilon()]),
        ProductionRule(MEMBERS, [MEMBER, ANOTHER_MEMBER]),
        ProductionRule(ANOTHER_MEMBER, [comma, MEMBER, ANOTHER_MEMBER]),
        ProductionRule(ANOTHER_MEMBER, [Epsilon()]),
        ProductionRule(MEMBER, [string, colon, ELEMENT]),
        ProductionRule(ARRAY, [left_square, ELEMENTS, right_square]),
        ProductionRule(ELEMENTS, [Epsilon()]),
        ProductionRule(ELEMENTS, [ELEMENT, ANOTHER_ELEMENT]),
        ProductionRule(ELEMENT, [VALUE]),
        ProductionRule(ANOTHER_ELEMENT, [comma, ELEMENT, ANOTHER_ELEMENT]),
        ProductionRule(ANOTHER_ELEMENT, [Epsilon()]),
    ]

    JSON_GRAMMAR = CFG(
        production_rules=PRODUCTION_RULES,
        alphabet=[chr(i) for i in range(128)],
        start_symbol=JSON,
    )
