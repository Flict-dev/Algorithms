# n = int(input())
# rows = [input() for _ in range(n)]
rows = [
    "..._.#.",
    ".##_...",
    ".#._.##",
    "..._...",
]

passengers = [
    "2 left aisle",
    "3 right window",
    "2 left window",
    "3 left aisle",
    "1 right window",
    "2 right window",
    "1 right window",
]

# m = int(input())
# passengers = [input() for _ in range(n)]
sym = {
    ".": 0,
    "#": 1,
}


r_data = {}
for i in range(len(rows)):
    sp_row = rows[i].split("_")
    left = [sym[_] for _ in sp_row[0]]
    right = [sym[_] for _ in sp_row[1]]
    r_data[i] = {"left": left, "right": right}
q_rows = len(rows)

"""
left

window [0:k] left left
aisle [-k:3] left right


right
window [-k:3] right right
aislew [0:k] right left
"""


def get_seats(seats: list, pos: str, place: str, k: int):
    # Our slice, remains, swap?
    x, y = (seats[0:k], seats[k:3], 0), (seats[-k:3], seats[0:-k], 1)
    w = ("A", "B", "C", "D", "E", "F")
    data = {
        "left": {
            "window": x,  # left left
            "aisle": y,  # left right
        },
        "right": {
            "window": y,  # right right
            "aisle": x,  # right left
        },
    }
    return data[pos][place]


for pas in passengers:
    c, pos, place = pas.split()
    res = []
    for row in range(q_rows):
        places = r_data[row][pos]
        seats, rem, switch = get_seats(places, pos, place, int(c))
        if sum(seats) == 0:
            seats = [1 for _ in range(len(seats))]
            r_data[row][pos] = rem + seats if switch else seats + rem
            break
print(r_data)
