string = "Hello World"

#
length = len(string)

print(length)

for i, num in enumerate(string):
  print(f"index {i}" )
  print(f"Hello World {str(num)}")

# listの実験
#
print(list(range(5, 5 + length)))

for i, num in enumerate(list(range(5, 5 + length))):
  print(f"i={i}, num={num}")
