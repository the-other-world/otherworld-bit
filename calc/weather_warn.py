import json

import numpy as np

from calc.temp import HOUR_OFFSET


def get_warn():
    f = open('data.json')
    data = json.load(f)
    warning = "无"
    if data["day_temp"] + np.max(HOUR_OFFSET) >= 40:
        warning = "高温红色预警"
    elif data["day_temp"] + np.max(HOUR_OFFSET) >= 37:
        warning = "高温橙色预警"
    elif data["high_temp_days"] >= 3:
        warning = "高温黄色预警"
    elif data["day_temp"] + np.min(HOUR_OFFSET) <= 0 \
            and (np.max(HOUR_OFFSET) * data["temp_multi"]) + data["fluctuation"] <= -16:
        warning = "寒潮红色预警"
    elif data["day_temp"] + np.min(HOUR_OFFSET) <= 0 \
            and (np.max(HOUR_OFFSET) * data["temp_multi"]) + data["fluctuation"] <= -12:
        warning = "寒潮橙色预警"
    elif data["day_temp"] + np.min(HOUR_OFFSET) <= 0 \
            and (np.max(HOUR_OFFSET) * data["temp_multi"]) + data["fluctuation"] <= -10:
        warning = "寒潮黄色预警"
    elif data["day_temp"] + np.min(HOUR_OFFSET) <= 4 \
            and (np.max(HOUR_OFFSET) * data["temp_multi"]) + data["fluctuation"] <= -8:
        warning = "寒潮蓝色预警"
    return warning
