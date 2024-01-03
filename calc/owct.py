import owtime


def get_time():
    owt = owtime.owtimes.OWTime.now()
    owts = owtime.owts.OWTS.now().timestamp
    return {
        "years": owt.year,
        "months": owt.month,
        "days": owt.day,
        "dayinweek": owt.weekday,
        "hours": owt.hour,
        "minutes": owt.minute,
        "seconds": owt.second,
        "milliseconds": owt.millisecond,
        "timestamp": owts
    }
