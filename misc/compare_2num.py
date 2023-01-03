def compare(x: str, y: str):

  def count_d(data: str):
    current = {}
    for i in data:
      if i not in current.keys():
        current[i] = 0
      current[i] += 1
    return current

  res1 = count_d(x)
  res2 = count_d(y)
  return res1 == res2

print(compare('20212', '1202'))