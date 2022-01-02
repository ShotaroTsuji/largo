from largo.pl_command import parse_argument, ArgumentType


def test_parse_argument():
    want = (ArgumentType.YEAR, 2021)
    got = parse_argument('2021')
    assert want == got

    want = (ArgumentType.MONTH, 'jan')
    got = parse_argument('jan')
    assert want == got
