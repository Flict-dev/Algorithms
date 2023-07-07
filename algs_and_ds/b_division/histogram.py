row = open("input.txt").read()

uniq = sorted(set(row.replace("\n", "").replace(" ", "")))

data = {i: row.count(uniq[i]) for i in range(len(uniq))}

m_column = max(data.values())

for i in range(m_column, 0, -1):
    row_s = ""
    for j in range(len(uniq)):
        if i <= data[j]:
            row_s += "#"
        else:
            row_s += " "
    print(row_s)
print("".join(uniq))
