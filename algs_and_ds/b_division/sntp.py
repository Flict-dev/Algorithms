times = [input() for _ in range(3)]

def time_to_seconds(time: str):
    hours, minutes, seconds = map(int, time.split(":"))
    return hours * 3600 + 60 * minutes + seconds


def seconds_to_time(seconds: int):
    hours, minutes, sec = (
        seconds // 3600 % 24,
        seconds // 60 % 60,
        seconds % 60,
    )

    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, sec)


a, b, c = map(time_to_seconds, times)
if c < a:
    c += time_to_seconds("24:00:00")

print(seconds_to_time(b + (c - a + 1) // 2))
