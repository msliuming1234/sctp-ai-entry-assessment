def convertTemp(value, unit):
    if unit == "C":
        result = (value * 9/5) + 32
    elif unit == "F":
        result = (value - 32) * 5/9
    else:
        return -1

    return round(result, 2)
