def weather_info(temp):
    c = convertToCelsius(temp)
    if (c < 0):
        return ("{} is freezing temperature".format(c))
    else:
        return ("{} is above freezing temperature".format(c))
    
def convertToCelsius(temp):
    return (temp - 32) * (float(5)/9)
