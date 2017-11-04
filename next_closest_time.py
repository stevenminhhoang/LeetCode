
import itertools
def next_closest_time(time):
    h, m = time.split(':')
    input_time = list(map(int, [h[0],h[1],m[0],m[1]]))
    hours = set((filter(check_valid, permutations(input_time))))
    hours.remove(tuple(input_time))
    if not hours:
        return to_str(to_minute(input_time))
    nearest_diff = 60*24
    ans = 0

    for i in hours:
        t = to_minute(i)
        # print(to_str(t))
        if t < to_minute(input_time):
            t += 60*24
        if t - to_minute(input_time) < nearest_diff :
            nearest_diff = t - to_minute(input_time)
            ans = t
    ans = (ans + 60*24) % (60*24)
    return to_str(ans)


def check_valid(t):
    hour = t[0]*10 + t[1]
    minute = t[2]*10 + t[3]
    return hour < 24 and minute < 60

def permutations(n):
    hours = list(itertools.product([n[0],n[1],n[2],n[3]],repeat=4))
    return hours

def to_minute(t):
    hour = t[0]*10 + t[1]
    minute = t[2]*10 + t[3]
    return hour*60 + minute

def to_str(m):
    return "{:02d}:{:02d}".format(*divmod(m,60))


print(next_closest_time("11:11"))
# print(to_minute([1,9,3,4]))
# print(to_str(1174))
