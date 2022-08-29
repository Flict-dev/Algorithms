words = input()
res = []
current = words[0]
quantity = 1

def pack(word, quantity):
  if quantity == 1:
    return word
  return word + str(quantity)

for i in range(1, len(words)):
  if words[i] == current:
    quantity += 1
  else:
      res.append(pack(current, quantity))
      quantity = 1
      current = words[i]
res.append(pack(current, quantity))
print(''.join(res))
    
