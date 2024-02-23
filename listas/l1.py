def valores(b):
  if b == 0:
    return 0
  return 1+ valores(b-1)
b = 1000
print(valores(b))
        
