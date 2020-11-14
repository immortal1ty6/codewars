def parse_float(string):
    try:
        if string:
            return float(string)
    except:
        return None
