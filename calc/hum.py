def get_hum(weather, last_preci):
    if weather == 4:
        return 1
    else:
        return 1 - (last_preci // 32768 * 0.02) if 1 - (last_preci // 32768 * 0.02) >= 0.3 and last_preci != 0 else 0.3
