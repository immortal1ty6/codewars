def areYouPlayingBanjo(name):
    if name.startswith("R") or name.startswith("r"):
        return "{} plays banjo".format(name)
    else:
        return "{} does not play banjo".format(name)
