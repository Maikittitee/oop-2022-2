def is_plusone_dictionary(d):
  temp = 0
  for a, b in d.items():
    if a + 1 != b or temp + 1 != a:
      return (False)
    temp = b
  return (True)


di = {1: 2, 3: 4, 5: 6, 7: 8}

print(is_plusone_dictionary(di))
