def unique_list(list):
  x = []
  for numb in list:
    if numb not in x:
      x.append(numb)
  return x

list = list(input("Input couple numbers: "))
print(unique_list(list))
