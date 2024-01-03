import json
import random

import numpy as np

from calc import owct

WIND_SPEED = [
    [0, 0.2],  # 0级
    [0.3, 1.5],  # 1级
    [1.6, 3.3],  # 2级
    [3.4, 5.4],  # 3级
    [5.5, 7.9],  # 4级
    [8, 10.7],  # 5级
    [10.8, 13.8],  # 6级
    [13.9, 17.1],  # 7级
    [17.2, 20.7],  # 8级
    [20.8, 24.4],  # 9级
    [24.5, 28.4],  # 10级
    [28.5, 32.6],  # 11级
    [32.7, 36.9]  # 12级
]


def get_wind():
    now = owct.get_time()
    f = open('data.json')
    data = json.load(f)
    if np.floor(now["timestamp"]) - data["cycle_now"] >= 16384:
        wind_scale = data["wind_scale"]
        if wind_scale > 3:
            random.seed(data["cycle_now"] + random.randint(-5, 5))
            for i in range(1, wind_scale - 3 + 1):
                percentage = 0.5 ** (data["wind_scale"] - (wind_scale - 1))
                choice = random.random()
                if wind_scale <= 3 or choice >= percentage:
                    break
                else:
                    wind_scale -= 1
        if wind_scale == 3:
            random.seed(data["cycle_now"] + random.randint(-5, 5))
            for i in range(9):
                if wind_scale == 12:
                    break
                else:
                    percentage = 0.5 ** (data["wind_scale"] - 2)
                    choice = random.random()
                    if choice >= percentage:
                        break
                    else:
                        wind_scale += 1
        else:
            wind_scale = random.randint(0, 3)
        data["wind_scale"] = wind_scale
        data["wind_speed"] = round(random.uniform(WIND_SPEED[wind_scale][0], WIND_SPEED[wind_scale][1]), 1)
        data["wind_direction"] = random.randint(0, 7)
        jobj = json.dumps(data, indent=4)
        with open("data.json", "w") as outfile:
            outfile.write(jobj)
