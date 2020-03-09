from languagetools.parser.cfg import CFG, Terminal, NonTerminal, ProductionRule
from languagetools.parser.cfg import Epsilon


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

    # # TERMINALS

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

    # # PRODUCTION RULES

    PRODUCTION_RULES = [
        ProductionRule(JSON, [VALUE], name="SKIP"),
        ProductionRule(VALUE, [OBJECT], name="SKIP"),
        ProductionRule(VALUE, [ARRAY], name="SKIP"),
        ProductionRule(VALUE, [string], name="SKIP"),
        ProductionRule(VALUE, [number], name="SKIP"),
        ProductionRule(VALUE, [true], name="SKIP"),
        ProductionRule(VALUE, [false], name="SKIP"),
        ProductionRule(VALUE, [null], name="SKIP"),
        ProductionRule(
            OBJECT, [left_curly, MEMBERS, right_curly], name="OBJECT_CREATE"
        ),
        ProductionRule(MEMBERS, [Epsilon()], name="SKIP"),
        ProductionRule(MEMBERS, [MEMBER, ANOTHER_MEMBER], name="SKIP"),
        ProductionRule(ANOTHER_MEMBER, [comma, MEMBER, ANOTHER_MEMBER], name="SKIP"),
        ProductionRule(ANOTHER_MEMBER, [Epsilon()], name="SKIP"),
        ProductionRule(MEMBER, [string, colon, ELEMENT], name="ADD_FIELD"),
        ProductionRule(
            ARRAY, [left_square, ELEMENTS, right_square], name="ARRAY_CREATE"
        ),
        ProductionRule(ELEMENTS, [Epsilon()], name="SKIP"),
        ProductionRule(ELEMENTS, [ELEMENT, ANOTHER_ELEMENT], name="SKIP"),
        ProductionRule(ELEMENT, [VALUE], name="SKIP"),
        ProductionRule(ANOTHER_ELEMENT, [comma, ELEMENT, ANOTHER_ELEMENT], name="SKIP"),
        ProductionRule(ANOTHER_ELEMENT, [Epsilon()], name="SKIP"),
    ]

    JSON_GRAMMAR = CFG(
        production_rules=PRODUCTION_RULES,
        alphabet=[chr(i) for i in range(128)],
        start_symbol=JSON,
    )
