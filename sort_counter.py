def sort_count(seq):
  maxs = max(seq)
  mins = min(seq)
  k = (maxs - mins + 1)
  data = [0] * k
  for now in seq:
    data[now - mins] += 1
  
  pos = 0
  
  for i in range(k):
    for _ in range(data[i]):
      seq[pos] = i + mins
      pos += 1
  return seq
print(sort_count([1, 8, 3, 4, 2, 2, 6, 6, 6, 6, 7 ]))