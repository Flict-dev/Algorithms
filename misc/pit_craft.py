data = [3, 1, 2]
maxpos = data.index(max(data))
pos = data[0]
res = 0
for i in data[:maxpos]:
    if i > pos:
      pos = i
    res  +=  pos - i
pos = 0
for i in reversed(data[maxpos:]):
    if i > pos:
      pos = i
    res += pos - i

print(res)