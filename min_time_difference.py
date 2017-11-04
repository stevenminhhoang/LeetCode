def min_time_diff(timePoints):
    minutes = list(map(to_minute, timePoints))
    minutes.sort()
    # return minutes
    return min((y-x) % (60*24) for x,y in zip(minutes,minutes[1:]+minutes[:1]))

def to_minute(t):
    h, m = map(int, t.split(':'))
    return h*60 + m


print(min_time_diff(["23:59","00:00","01:00"]))
