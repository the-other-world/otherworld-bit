import json
import random

import numpy as np

from calc import owct

BASELINE_TEMP = 15
GREENHOUSE_INDEX = 1 + (owct.get_time()["years"] - 2930) * 0.0005 if owct.get_time()["years"] < 3124 else 1.0975
SEASONS = [
    [3, 4],
    [5, 6],
    [7, 8],
    [1, 2]
]
TEMP_COEFFICIENT = [1.2, 2.0, 1.0, -0.4]
STD_DEVIATION = 5
HOUR_OFFSET = [0, 2, 5, 4, 0, -2, -3, -3]
HOUR_FLUCTUATION = 0.5


def get_temp():
    now = owct.get_time()
    for season in SEASONS:
        if now["months"] in season:
            f = open('data.json')
            data = json.load(f)
            avg_temp = BASELINE_TEMP * GREENHOUSE_INDEX * TEMP_COEFFICIENT[SEASONS.index(season)]
            random.seed(data["collected_at"])
            if random.random() < 0.5:
                day_temp = random.uniform(avg_temp - STD_DEVIATION, avg_temp)
            else:
                day_temp = random.uniform(avg_temp, avg_temp + STD_DEVIATION)
            if np.floor(now["timestamp"]) - data["collected_at"] >= 524288:
                data["day_temp"] = round(day_temp, 2)
                if data["day_temp"] + np.max(HOUR_OFFSET) >= 35:
                    data["high_temp_days"] += 1
                else:
                    data["high_temp_days"] = 0
            if np.floor(now["timestamp"]) - data["cycle_now"] >= 16384:
                current_cycle = int(np.floor((now["hours"] - 8) / 4))
                random.seed(current_cycle)
                fluctuation = round(random.uniform(0 - HOUR_FLUCTUATION, HOUR_FLUCTUATION), 2)
                multi = round(random.uniform(random.random(), 1 / random.random()), 2)
                data["cycle_temp"] = round(data["day_temp"]
                                           + (multi * HOUR_OFFSET[current_cycle])
                                           + fluctuation, 2)
                data["fluctuation"] = fluctuation
                data["temp_multi"] = multi
            jobj = json.dumps(data, indent=4)
            with open("data.json", "w") as outfile:
                outfile.write(jobj)
            return data["cycle_temp"]
