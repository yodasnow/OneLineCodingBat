def squirrel_play(temp, is_summer):
    return (not is_summer and temp<=90 and temp>=60) or (is_summer and temp<=100 and temp>=60)