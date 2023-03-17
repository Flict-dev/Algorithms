s = input()

res = {key: s.count(key) for key in set(s)}

s_len = len(s)
for i in range():
    a, b = i, s_len - i - 1
    res[s[i]] += b + a + a * b

for i in sorted(res):
    print(f"{i}: {res[i]}")
