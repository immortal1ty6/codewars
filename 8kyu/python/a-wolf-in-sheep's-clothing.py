def warn_the_sheep(queue):
    queue.reverse()
    wolf_pos = queue.index("wolf")
    if wolf_pos == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return "Oi! Sheep number " + str(wolf_pos) + "! You are about to be eaten by a wolf!"
