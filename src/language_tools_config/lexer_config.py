from langtools.lexer.basic_symbols import (
    DIGITS,
    NON_ZERO_DIGITS,
    ASCII,
)
from langtools.lexer.dfa import DFA
from langtools.lexer.nfa import Atom, Concat, Epsilon, KleeneStar, Union
from src.language_tools_config.tokens import (
    ColonToken,
    CommaToken,
    FalseToken,
    LeftCurlyToken,
    LeftSquareToken,
    NullToken,
    NumberToken,
    RightCurlyToken,
    RightSquareToken,
    StringToken,
    TrueToken,
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

    # Strings

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

    _hex_number = Concat(
        Atom("u"),
        _hex_digit,
        _hex_digit,
        _hex_digit,
        _hex_digit,
        _hex_digit,
        _hex_digit,
    )

    _escaped_char = Concat(
        Atom("\\"),
        Union(
            Atom("/"),
            Atom("\\"),
            Atom("b"),
            Atom("f"),
            Atom("n"),
            Atom("r"),
            Atom("t"),
            Atom('"'),
            _hex_number,
        ),
    )

    STRING = Concat(
        Atom('"'),
        Union(
            Epsilon(),
            KleeneStar(
                Union(
                    *[
                        value
                        for key, value in ASCII.items()
                        if key != '"' and key != "\\"
                    ],
                    _escaped_char
                )
            ),
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
            COLON,
            COMMA,
            FALSE,
            LEFT_CURLY,
            LEFT_SQUARE,
            NULL,
            NUMBER,
            RIGHT_CURLY,
            RIGHT_SQUARE,
            STRING,
            TRUE,
            close=False,
        )
    )
