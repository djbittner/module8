"""
Author:  Derek Bittner
Due Date: 10/20/2020
Program: half_birthday.py

"""

from datetime import datetime, timedelta


def half_birthday(year, month, day):
    bday = datetime(year=year, month=month, day=day)
    half_bday = timedelta(days=182)
    result = bday + half_bday
    return result


if __name__ == '__main__':
    print("Derek's half birthday is: ", half_birthday(2020, 7, 19))
