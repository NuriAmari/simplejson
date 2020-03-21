from langtools.lexer.basic_symbols import (
    DIGITS,
    NON_ZERO_DIGITS,
    ASCII,
)
from langtools.lexer.nfa import Atom, Concat, Epsilon, KleeneStar, Union
from langtools.lexer.dfa import DFA
from src.language_tools_config.tokens import (
    CommaToken,
    ColonToken,
    LeftCurlyToken,
    RightCurlyToken,
    LeftSquareToken,
    RightSquareToken,
    NumberToken,
    StringToken,
    TrueToken,
    FalseToken,
    NullToken,
)


class LexerConfig:

    # General

    _period = Atom(".")
    COMMA = Atom(",")
    COMMA.add_token(CommaToken)
    COLON = Atom(":")
    COLON.add_token(ColonToken)
    LEFT_CURLY = Atom("{")
    LEFT_CURLY.add_token(LeftCurlyToken)
    RIGHT_CURLY = Atom("}")
    RIGHT_CURLY.add_token(RightCurlyToken)
    LEFT_SQUARE = Atom("[")
    LEFT_SQUARE.add_token(LeftSquareToken)
    RIGHT_SQUARE = Atom("]")
    RIGHT_SQUARE.add_token(RightSquareToken)

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
    NUMBER.add_token(NumberToken)

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
    STRING.add_token(StringToken)

    # Booleans

    TRUE = Concat(Atom("t"), Atom("r"), Atom("u"), Atom("e"))
    TRUE.add_token(TrueToken)
    FALSE = Concat(Atom("f"), Atom("a"), Atom("l"), Atom("s"), Atom("e"))
    FALSE.add_token(FalseToken)

    # Miscelaneous

    NULL = Concat(Atom("n"), Atom("u"), Atom("l"), Atom("l"))
    NULL.add_token(NullToken)

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
