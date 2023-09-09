from datetime import datetime, timezone
import json
import random
import numpy as np

import calc.owct

BASELINE_TEMP = 15
SEASONS = [
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11],
    [12, 1, 2]
]
TEMP_COEFFICIENT = [1.2, 2.0, 1.0, -0.4]
STD_DEVIATION = 5
HOUR_OFFSET = [0, 2, 5, 4, 0, -2, -3, -3]


def get_temp():
    now = calc.owct.get_time()
    utcnow = datetime.now(timezone.utc)
    print(now)
    for season in SEASONS:
        if now.month in season:
            avg_temp = int(BASELINE_TEMP * TEMP_COEFFICIENT[SEASONS.index(season)])
            day_temp = random.uniform(avg_temp - STD_DEVIATION, avg_temp + STD_DEVIATION)
            f = open('data.json')
            data = json.load(f)
            if np.floor(utcnow.timestamp()) - data["collected_at"] >= 86400:
                data["collected_at"] = np.floor(utcnow.timestamp()) - (np.floor(utcnow.timestamp()) % 86400)
                data["cycle_0"] = np.floor(utcnow.timestamp()) - (np.floor(utcnow.timestamp()) % 86400) + 28800
                data["day_temp"] = day_temp
                if data["day_temp"] + np.max(HOUR_OFFSET) >= 35:
                    data["high_temp_days"] += 1
                else:
                    data["high_temp_days"] = 0
            if np.floor(utcnow.timestamp()) - data["cycle_now"] >= 3600:
                current_cycle = int(np.floor((now.hour - 8) / 3))
                data["cycle_now"] = np.floor(utcnow.timestamp() - (np.floor(utcnow.timestamp()) % 3600))
                data["cycle_temp"] = data["day_temp"] + (random.uniform(0.8, 1.2) * HOUR_OFFSET[current_cycle])
            jobj = json.dumps(data, indent=4)
            with open("data.json", "w") as outfile:
                outfile.write(jobj)
            return np.round(data["cycle_temp"], 2)


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
    elif np.min(HOUR_OFFSET) - np.max(HOUR_OFFSET) <= -16 and data["day_temp"] + np.min(HOUR_OFFSET) <= 0:
        warning = "寒潮红色预警"
    elif np.min(HOUR_OFFSET) - np.max(HOUR_OFFSET) <= -12 and data["day_temp"] + np.min(HOUR_OFFSET) <= 0:
        warning = "寒潮橙色预警"
    elif np.min(HOUR_OFFSET) - np.max(HOUR_OFFSET) <= -10 and data["day_temp"] + np.min(HOUR_OFFSET) <= 4:
        warning = "寒潮黄色预警"
    elif np.min(HOUR_OFFSET) - np.max(HOUR_OFFSET) <= -8 and data["day_temp"] + np.min(HOUR_OFFSET) <= 4:
        warning = "寒潮蓝色预警"
    return warning
