"""
Ищет наилучшую комбинацию вещей, 
которые могут посместиться в указанный объём. 

В этом слуачае объём равен 6
"""

things = {
    1: {"w": 3, "a": 10, "n": "water:  "},
    2: {"w": 1, "a": 3, "n": "book:   "},
    3: {"w": 2, "a": 9, "n": "food:   "},
    4: {"w": 2, "a": 5, "n": "jacket: "},
    5: {"w": 1, "a": 6, "n": "camera: "},
}


data = {row: {column: 0 for column in range(1, 7)} for row in range(1, 6)}

# j - weight i - thing
# j - column i - row

for i in range(1, 6):
    thing = things[i]
    for j in range(1, 7):
        # check for first row
        if i == 1:
            if j >= things[i]["w"]:
                data[i][j] = things[i]["a"]
        else:
            k = j - thing["w"]
            # check weight if weight < 0 or weight == 0: => thing weight == 1 or == current weight
            if k <= 0:
                if data[i - 1][j] < thing["a"]:
                    data[i][j] = thing["a"]
                else:
                    data[i][j] = data[i - 1][j]
            else:
                if data[i - 1][j] < data[i][k] + thing["a"]:
                    data[i][j] = thing["a"] + data[i - 1][j - thing["w"]]
                else:
                    data[i][j] = data[i - 1][j]


def dprint(data: dict):
    for i in range(1, 6):
        row = things[i]["n"]
        for j in range(1, 7):
            row += str(data[i][j]) + " "
        print(row, end="\n")


dprint(data)

# The biggest sequence
"""
Будущему мне 

Здесь важно то, что мы ищем наибольшую ПОСЛЕДОВАТЕЛЬНОСТЬ

Выбор максимума в else нужен для того, 
чтобы в таблице всегда и везде был максимум последовательности, 
чтобы в любой момент его можно было увеличить если буквы равны
"""
word1 = "fosh"
word2 = "foft"

data = {row: {column: 0 for column in range(len(word1))} for row in range(len(word2))}

rword1 = range(len(word1))
rword2 = range(len(word2))

for i in rword1:
    for j in rword2:
        if word2[i] == word1[j]:
            if i - 1 in rword1 and j - 1 in rword2:
                data[i][j] = data[i - 1][j - 1] + 1
            else:
                data[i][j] = 1
        else:
            if i - 1 in rword1 and j - 1 in rword2:
                data[i][j] = max(data[i - 1][j], data[i][j - 1])
            elif i - 1 in rword1:
                data[i][j] = data[i - 1][j]
            elif j - 1 in rword2:
                data[i][j] = data[i][j - 1]
            else:
                data[i][j] = 0


print(" ", " ".join(word1))
for i in range(len(word2)):
    r = ""
    for j in range(len(word1)):
        r += f"{data[i][j]} "
    print(f"{word2[i]} {r}")
