from math import *
from datetime import datetime


def get_time():
    owts = floor(datetime.utcnow().timestamp() * 1000) - 1679295600000
    days_elapsed = floor(owts / 1000 / 524288)
    year = floor(days_elapsed / 256)
    month = floor(((days_elapsed - year * 256) / 32))
    week = floor(((days_elapsed - year * 256) / 8))
    day = floor((days_elapsed - year * 256 - month * 32))
    dayinweek = days_elapsed % 8
    remaining_milliseconds = owts % 524288000
    hour = floor((remaining_milliseconds / 1000) / 16384)
    minute = floor(((remaining_milliseconds / 1000) - hour * 16384) / 128)
    second = floor((remaining_milliseconds / 1000) - hour * 16384 - minute * 128)
    millisecond = floor(remaining_milliseconds - hour * 16384000 - minute * 128000 - second * 1000)
    return {
        "years": year + 3047,
        "months": month + 1,
        "weeks": week + 1,
        "days": day + 1,
        "dayinweek": dayinweek,
        "hours": hour,
        "minutes": minute,
        "seconds": second,
        "milliseconds": millisecond,
        "timestamp": owts
    }
