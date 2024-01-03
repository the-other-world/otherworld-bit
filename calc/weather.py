import json
import random

import numpy as np

import calc.hum
from calc import owct, temp, wind, weather_warn


WEATHER = [
    "晴",
    "多云",
    "阴",
    "雾",
    "雨"
]

PRECIPITATION = [
    [0.1, 4.9, "小"],
    [5.0, 14.9, "中"],
    [15.0, 29.9, "大"],
    [30, 69.9, "暴"],
    [70, 139.9, "大暴"],
    [140.0, 249.9, "特大暴"],
    [250.0, 999.9, "史无前例的"]
]

WIND_DIRECTION = [
    "北",
    "东北",
    "东",
    "东南",
    "南",
    "西南",
    "西",
    "西北",
]


def get_weather():
    temp.get_temp()
    wind.get_wind()
    now = owct.get_time()
    f = open('data.json')
    data = json.load(f)
    data["collected_at"] = np.floor(now["timestamp"]) - (np.floor(now["timestamp"]) % 524288)
    data["cycle_0"] = np.floor(now["timestamp"]) - (np.floor(now["timestamp"]) % 524288) + 131072
    weather = data["weather"]
    if np.floor(now["timestamp"]) - data["cycle_now"] >= 16384:
        cycle_now = np.floor(now["timestamp"] - (np.floor(now["timestamp"]) % 16384))
        data["cycle_now"] = cycle_now
        random.seed(cycle_now)
        weather = round(random.random() * 100) % len(WEATHER)
        random.seed(cycle_now + 3)
        preci_chance = round(random.random(), 1)
        preci_level = 0
        last_preci = 0
        precipitation = 0
        random.seed(cycle_now + 1)
        if random.random() < preci_chance or weather == 4:
            last_preci = now["timestamp"]
            weather = 4
            preci_level = 1
            for i in range(7):
                percentage = (1 / 2.5) ** preci_level
                random.seed(cycle_now + random.randint(-10, 10))
                choice = random.random()
                if choice < percentage:
                    preci_level += 1
                else:
                    break
            precipitation = round(random.uniform(
                PRECIPITATION[preci_level - 1][0], PRECIPITATION[preci_level - 1][1]), 1)
        data["weather"] = weather
        data["last_preci"] = last_preci
        data["cycle_hum"] = calc.hum.get_hum(weather, last_preci)
        data["preci_chance"] = preci_chance
        data["preci_level"] = preci_level
        data["precipitation"] = precipitation
    jobj = json.dumps(data, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(jobj)
    return {
        "temp": data["cycle_temp"],
        "wind_scale": data["wind_scale"],
        "wind_speed": data["wind_speed"],
        "wind_direction": WIND_DIRECTION[data["wind_direction"]],
        "warnings": weather_warn.get_warn(),
        "weather": f"{PRECIPITATION[data['preci_level'] - 1][2]}雪"
        if data["weather"] == 4 and data["cycle_temp"] <= 0 else
        WEATHER[data["weather"]] if weather != 4 else
        f"{PRECIPITATION[data['preci_level'] - 1][2]}{WEATHER[data['weather']]}",
        "preci_chance": data["preci_chance"],
        "precipitation": data["precipitation"],
        "cycle_hum": data['cycle_hum']
    }
