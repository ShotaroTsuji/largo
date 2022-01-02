from largo.pl_command import Month


def test_parse_month_string():
    table = [('jan', 1), ('feb', 2), ('mar', 3), ('apr', 4), ('may', 5), ('jun', 6), ('jul', 7),
             ('aug', 8), ('sep', 9), ('oct', 10), ('nov', 11), ('dec', 12)]
    for s, want in table:
        month = Month(s)
        got = int(month)
        assert want == got
        got = str(month)
        assert s == got


def test_month_to_range_str():
    table = [('jan', ('jan', 'feb')), ('may', ('may', 'jun')), ('dec', ('dec', None))]
    for s, want in table:
        month = Month(s)
        got = month.to_range_str()
        assert want == got
