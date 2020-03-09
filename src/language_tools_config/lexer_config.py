from languagetools.lexer.basic_symbols import (
    DIGITS,
    NON_ZERO_DIGITS,
    ALPHABET,
    UPPERCASE_ALPHABET,
    ASCII,
)
from languagetools.lexer.nfa import Atom, Concat, Epsilon, KleeneStar, Union
from languagetools.lexer.dfa import DFA
from languagetools.lexer.token import Token


class LexerConfig:

    # General

    _period = Atom(".")
    COMMA = Atom(",")
    COMMA.end_state.tokens.add(Token(name="COMMA"))
    COLON = Atom(":")
    COLON.end_state.tokens.add(Token(name="COLON"))
    LEFT_CURLY = Atom("{")
    LEFT_CURLY.end_state.tokens.add(Token(name="LEFT_CURLY"))
    RIGHT_CURLY = Atom("}")
    RIGHT_CURLY.end_state.tokens.add(Token(name="RIGHT_CURLY"))
    LEFT_SQUARE = Atom("[")
    LEFT_SQUARE.end_state.tokens.add(Token(name="LEFT_SQUARE"))
    RIGHT_SQUARE = Atom("]")
    RIGHT_SQUARE.end_state.tokens.add(Token(name="RIGHT_SQUARE"))

    # Numbers

    _minus = Atom("-")
    _plus = Atom("+")
    _sign = Union(Epsilon(), _minus, _plus)

    _unsigned_integer = Union(
        Union(*DIGITS), Concat(Union(*NON_ZERO_DIGITS), KleeneStar(Union(*DIGITS)))
    )
    _integer = Concat(Union(_minus, Epsilon()), _unsigned_integer)

    _digits = KleeneStar(Union(*DIGITS))
    _fraction = Union(Epsilon(), Concat(_period, _digits))
    _exponent = Union(
        Epsilon(), Concat(Atom("E"), _sign, _digits), Concat(Atom("e"), _sign, _digits)
    )

    NUMBER = Concat(_integer, _fraction, _exponent)
    NUMBER.end_state.tokens.add(Token(name="NUMBER"))

    _hex_digit = Union(
        Atom("A"),
        Atom("B"),
        Atom("C"),
        Atom("D"),
        Atom("E"),
        Atom("F"),
        Atom("a"),
        Atom("b"),
        Atom("c"),
        Atom("d"),
        Atom("e"),
        Atom("f"),
        Union(*NON_ZERO_DIGITS),
    )

    # Strings
    STRING = Concat(
        Atom('"'),
        Union(
            Epsilon(),
            KleeneStar(Union(*[value for key, value in ASCII.items() if key != '"'])),
        ),
        Atom('"'),
    )
    STRING.end_state.tokens.add(Token(name="STRING"))

    # Booleans

    TRUE = Concat(Atom("t"), Atom("r"), Atom("u"), Atom("e"))
    TRUE.end_state.tokens.add(Token(name="TRUE"))
    FALSE = Concat(Atom("f"), Atom("a"), Atom("l"), Atom("s"), Atom("e"))
    FALSE.end_state.tokens.add(Token(name="FALSE"))

    # Miscelaneous

    NULL = Concat(Atom("n"), Atom("u"), Atom("l"), Atom("l"))
    NULL.end_state.tokens.add(Token(name="NULL"))

    TOKENIZER = DFA(
        Union(
            NUMBER,
            STRING,
            COMMA,
            COLON,
            LEFT_CURLY,
            RIGHT_CURLY,
            LEFT_SQUARE,
            RIGHT_SQUARE,
            TRUE,
            FALSE,
            NULL,
            close=False,
        )
    )
