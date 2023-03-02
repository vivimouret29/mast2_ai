from unittest.mock import MagicMock

import leap_years as leap_years

def test_if_year_is_divisible_by_400():
    assert (leap_years.year_is_divisible_by_400(2000) == True)