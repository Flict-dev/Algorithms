from collections import Counter

n = int(input())
row = input()
k = n
row_counter = Counter(row)

data = list(row_counter.keys())
left, right = 0, 0
maximum = 0


if k == 0:
    print(row_counter.most_common(1)[0][1])
    exit()


for cur in data:
    while right != len(row):
        if k >= 0:
            if row[right] != cur:
                k -= 1
            right += 1
            if k == 0:
                if maximum < right - left:
                    maximum = right - left
        elif k < 0:
            if row[left] != cur:
                k += 1
            left += 1
    left, right, k = 0, 0, n
print(maximum)
