from datetime import datetime

import ntplib


def get_time():
    ntp = ntplib.NTPClient()
    ntp_response = ntp.request('owct.khbit.cn', version=3)
    if ntp_response:
        return datetime.fromtimestamp(ntp_response.tx_time)
