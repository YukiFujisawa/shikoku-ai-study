# num = 0

# range(stop)
for num in range(5):
  print("hello world" + str(num))

print("# 5〜10")

# range(start, stop)
for num in range(5, 10):
  print("hello world" + str(num))

print("# 2ステップ")

# range(start, stop, step)
for num in range(5, 10 , 2):
  print("hello world" + str(num))

print("# 逆順")

# range(start, stop, -step)
for num in range(10, 0 , -1):
  print("hello world" + str(num))

print("# list")

# list(start, stop, -step)

print(type(range(5)))
print(type(list(range(5))))
print(list(range(5)))

list1 = list(range(5))
for item in list1:
  print("hello world" + str(item))