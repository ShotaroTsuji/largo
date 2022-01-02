from largo.date_range import DateRange


def test_date_range():
    table = [(DateRange(2021), '2021-01-01', '2022-01-01'),
             (DateRange(2021, 'jan'), '2021-01-01', '2021-02-01'),
             (DateRange(2021, 'dec'), '2021-12-01', '2022-01-01')]

    for dr, begin, end in table:
        assert str(dr.begin) == begin
        assert str(dr.end) == end
