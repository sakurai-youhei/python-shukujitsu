# python-shukujitsu
Python Japanese holidays library based on static data published by Cabinet Office, Government of Japan

[![PyPI License        ](https://img.shields.io/pypi/l/python-shukujitsu.svg)](https://pypi.org/project/python-shukujitsu/)
[![PyPI Downloads      ](https://img.shields.io/pypi/dm/python-shukujitsu.svg)](https://pypi.org/project/python-shukujitsu/)
[![PyPI Version        ](https://img.shields.io/pypi/v/python-shukujitsu.svg)](https://pypi.org/project/python-shukujitsu/)
[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/python-shukujitsu.svg)](https://pypi.org/project/python-shukujitsu/)

[![flake8 and pytest   ](https://github.com/sakurai-youhei/python-shukujitsu/workflows/flake8%20and%20pytest/badge.svg)](https://github.com/sakurai-youhei/python-shukujitsu/actions?query=workflow%3A%22flake8+and+pytest%22)
[![Publish to PyPI     ](https://github.com/sakurai-youhei/python-shukujitsu/workflows/Publish%20to%20PyPI/badge.svg)](https://github.com/sakurai-youhei/python-shukujitsu/actions?query=workflow%3A%22Publish+to+PyPI%22)
[![Publish to DockerHub](https://github.com/sakurai-youhei/python-shukujitsu/workflows/Publish%20to%20DockerHub/badge.svg)](https://github.com/sakurai-youhei/python-shukujitsu/actions?query=workflow%3A%22Publish+to+DockerHub%22)
[![RPM and DEB         ](https://github.com/sakurai-youhei/python-shukujitsu/workflows/RPM%20and%20DEB/badge.svg)](https://github.com/sakurai-youhei/python-shukujitsu/actions?query=workflow%3A%22RPM+and+DEB%22)
[![CodeQL              ](https://github.com/sakurai-youhei/python-shukujitsu/workflows/CodeQL/badge.svg)](https://github.com/sakurai-youhei/python-shukujitsu/actions?query=workflow%3ACodeQL)

Usage is similar to [python-holidays](https://github.com/dr-prodigy/python-holidays) package. But note that this [python-shukujitsu](https://github.com/sakurai-youhei/python-shukujitsu) package covers only holidays in Japan **from the year 1955 to 2022** as of today.

```python
import shukujitsu

jp_holidays = shukujitsu.Japan()
# or:
# jp_holidays = shukujitsu.JP()
# or:
# jp_holidays = shukujitsu.CountryHoliday('JP')

from datetime import date

date(2020, 7, 24) in jp_holidays  # True
date(2019, 7, 24) in jp_holidays  # False

# The Holiday class will also recognize strings of any format
# and int/float representing a Unix timestamp
'2014-01-01' in jp_holidays  # True
'1/1/2014' in jp_holidays    # True
1388597445 in jp_holidays    # True

jp_holidays.get('2014-01-01')  # "元日"

jp_holidays['2014-01-01': '2014-01-03']  # [date(2014, 1, 1)]
```

## Installation

```
pip3 install python-shukujitsu
```

## Command-Line interface

`shukujitsu` command becomes available by installing this [python-shukujitsu](https://github.com/sakurai-youhei/python-shukujitsu) package.

```console
$ shukujitsu --help  # or python3 -m shukujitsu --help
usage: shukujitsu [-h] [-i] [-n] [-V] [DATE ...]

Utility to match Japanese holidays from the year 1955 to 2021

positional arguments:
  DATE                date to be matched

optional arguments:
  -h, --help          show this help message and exit
  -i, --invert-match  select non-matching dates
  -n, --holiday-name  output holiday name instead
  -V, --version       display version information and exit

Exit status stays 0 if one or more dates are matched. Otherwise, it always goes 1.
```

One or some dates can be input to the command through command-line arguments or STDIN.

```console
$ # You can start a conditional branch from shukujitsu command.
$ shukujitsu 2020-01-01 && echo This is a holiday || echo This is not a holiday
2020-01-01
This is a holiday

$ # You can also filter dates by using shukujitsu command.
$ cat <<EOF | shukujitsu > holidays.txt
> 2020-05-02
> 2020-05-03
> 2020-05-04
> 2020-05-05
> 2020-05-06
> 2020-05-07
> EOF

$ # You can check multiple dates at once.
$ shukujitsu 2020/7/22 2020/7/23 2020/7/24
2020/7/23
2020/7/24

$ # You can also check the name of each holiday.
$ shukujitsu -n 2020/7/22 2020/7/23 2020/7/24
海の日
スポーツの日

$ # You can also pick up non-holiday.
$ shukujitsu -i 2020/7/22 2020/7/23 2020/7/24
2020/7/22
```

## Alternative ways

### Docker

[![Docker Pulls](https://img.shields.io/docker/pulls/sakuraiyouhei/shukujitsu)](https://hub.docker.com/r/sakuraiyouhei/shukujitsu/)
[![Image Size  ](https://img.shields.io/docker/image-size/sakuraiyouhei/shukujitsu)](https://hub.docker.com/r/sakuraiyouhei/shukujitsu/)

```console
$ docker run -it sakuraiyouhei/shukujitsu --help
```

### yum

```console
$ sudo yum install -y curl
$ curl -fsSL https://sakurai-youhei.github.io/python-shukujitsu/rpm/python-shukujitsu.repo | sudo tee /etc/yum.repos.d/python-shukujitsu.repo
$ sudo yum install -y python-shukujitsu
$ shukujitsu --help
```

### apt

```console
$ sudo apt install -y curl gpg
$ curl -fsSL https://sakurai-youhei.github.io/python-shukujitsu/gpg | sudo apt-key add -
$ curl -fsSL https://sakurai-youhei.github.io/python-shukujitsu/deb/python-shukujitsu.list | sudo tee /etc/apt/sources.list.d/python-shukujitsu.list
$ sudo apt update
$ sudo apt install -y python-shukujitsu
$ shukujitsu --help
```

## Important Notice

### Source Data

This [python-shukujitsu](https://github.com/sakurai-youhei/python-shukujitsu) package bundles the following data. (Japanese - 本ライブラリは以下のデータを同梱しています。) The license of Source Data is [CC BY](https://creativecommons.org/licenses/by/4.0/legalcode.ja) compatible; The exact conditions are described at [内閣府ホームページ利用規約](https://www.cao.go.jp/notice/rule.html).

- 2021年2月1日時点の[内閣府ホームページ](https://www.cao.go.jp/)の[「国民の祝日」について](https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html)で公開されていた「[昭和30年（1955年）から令和4年（2022年）国民の祝日（csv形式：19KB）](https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv)」（内閣府） （[https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv](https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv)）
- 2020年11月27日時点の[内閣府ホームページ](https://www.cao.go.jp/)の[「国民の祝日」について](https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html)で公開されていた「[昭和30年（1955年）から令和3年（2021年）国民の祝日（csv形式：19KB）](https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv)」（内閣府） （[https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv](https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv)）
- 2020年11月18日時点の[内閣府ホームページ](https://www.cao.go.jp/)の[「国民の祝日」について](https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html)で公開されていた「[昭和30年（1955年）から令和3年（2021年）国民の祝日（csv形式：19KB）](https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv)」（内閣府） （[https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv](https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv)）

### Source Code

This [python-shukujitsu](https://github.com/sakurai-youhei/python-shukujitsu) package may contain a copy of and/or modified code from [python-holidays](https://github.com/dr-prodigy/python-holidays) package which is also licensed under [MIT License](https://github.com/dr-prodigy/python-holidays/blob/master/LICENSE).

### Relation to the Government of Japan

Nothing - NEVER EVER imagine relation to Government of Japan. This is just a personal project.
