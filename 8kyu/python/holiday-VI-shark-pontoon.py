def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2
        
    shark_eat_time = shark_distance / shark_speed
    you_safe_time = pontoon_distance / you_speed
    
    return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"
