from datetime import date
from datetime import datetime
from os.path import abspath
from os.path import dirname
from os.path import join
from sys import version_info
from unittest import main
from unittest import TestCase
from urllib.request import urlopen

from python_wrap_cases import wrap_case

import shukujitsu
from shukujitsu.data import load_bin
from shukujitsu.holidays import JapaneseHolidays


@wrap_case
class HolidaysTest(TestCase):
    @wrap_case(date(2020, 7, 24), True)
    @wrap_case(date(2019, 7, 24), False)
    @wrap_case("2014-01-01", True)
    @wrap_case("1/1/2014", True)
    @wrap_case("1/1/2014 12:34:56", True)
    @wrap_case("2/1/2014 12:34:56", False)
    @wrap_case("1/2/2014 12:34:56", False)
    @wrap_case(1388597445, True)
    @wrap_case(1388597445.1, True)
    @wrap_case("20200320", True)
    @wrap_case(date(2020, 3, 20), True)
    @wrap_case(datetime(2020, 3, 20), True)
    @wrap_case(datetime(2022, 4, 29), True)
    @wrap_case(datetime(2022, 5, 3), True)
    @wrap_case(datetime(2022, 5, 4), True)
    @wrap_case(datetime(2022, 5, 5), True)
    @wrap_case(datetime(2023, 5, 5), True)
    @wrap_case(datetime(2024, 5, 5), True)
    @wrap_case(datetime(2025, 5, 5), False)  # No data for holidays in 2025
    def test_holidays(self, day, expect):
        if expect:
            self.assertIn(day, JapaneseHolidays())
        else:
            self.assertNotIn(day, JapaneseHolidays())

    @wrap_case("2014-01-01", "元日")
    @wrap_case("2024-01-08", "成人の日")
    def test_holidays_get(self, day, expect):
        self.assertEqual(JapaneseHolidays().get(day), expect)

    @wrap_case("2014-01-01", "2014-01-03", None,
               [date(2014, 1, 1)])
    @wrap_case("2020/5/3", "2020/5/7", None,
               [date(2020, 5, day) for day in range(3, 7)])
    @wrap_case("2020/5/3", "2020/5/7", 2,
               [date(2020, 5, day) for day in range(3, 7, 2)])
    @wrap_case("2020/5/3", "2020/5/7", -1,
               [date(2020, 5, day) for day in range(3, 7, -1)])
    @wrap_case("2021/5/5", "2021/5/1", None,
               [date(2021, 5, day) for day in range(5, 2)])
    @wrap_case("2024/5/3", "2024/5/7", None,
               [date(2024, 5, day) for day in range(3, 7)])
    def test_holidays_slice(self, start, stop, step, expect):
        self.assertEqual(JapaneseHolidays()[slice(start, stop, step)], expect)

    @wrap_case(1990)
    @wrap_case(2018)
    @wrap_case(2019)
    def test_holidays_year(self, yyyy):
        for holiday in JapaneseHolidays()._year(yyyy):
            self.assertEqual(holiday.year, yyyy)


@wrap_case
class ExportsTest(TestCase):
    @wrap_case("JP")
    @wrap_case("JPN")
    def test_alias(self, alias):
        self.assertEqual(shukujitsu.Japan, getattr(shukujitsu, alias))

    @wrap_case("Japan")
    @wrap_case("JP")
    @wrap_case("JPN")
    def test_CountryHoliday(self, country):
        self.assertEqual(shukujitsu.Japan(),
                         shukujitsu.CountryHoliday(country))

    @wrap_case([])
    @wrap_case([2018])
    @wrap_case([2019, 2020, 2021])
    def test_CountryHoliday_years(self, years):
        holidays = shukujitsu.CountryHoliday("JPN", years=years)
        if years:
            for holiday in holidays:
                self.assertIn(holiday.year, years)
        else:
            self.assertGreater(len(set(h.year for h in holidays)), 1)

    @wrap_case(RuntimeError, "US", [])
    @wrap_case(ValueError, "JPN", "illegal")
    @wrap_case(RuntimeError, "JPN", [], "illegal")
    @wrap_case(RuntimeError, "JPN", [], illegal="illegal")
    def test_CountryHoliday_illegal_arguments(self, raises, country, years,
                                              *args, **kwargs):
        with self.assertRaises(raises):
            shukujitsu.CountryHoliday(country, years, *args, **kwargs)


class DataTest(TestCase):
    def test_bundled_data_with_the_one_on_web(self):
        URL = "https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv"
        with urlopen(URL) as res:
            self.assertEqual(load_bin(), res.read())


class SetupPyTest(TestCase):
    classifier = "Programming Language :: Python :: %s.%s" % version_info[:2]

    def test_classifiers_version(self):
        here = dirname(abspath(__file__))
        with open(join(here, "setup.py")) as fp:
            self.assertIn(SetupPyTest.classifier, fp.read())


if __name__ == "__main__":
    main(verbosity=2)
