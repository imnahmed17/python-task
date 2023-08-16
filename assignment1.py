import random

car = dict(brand = "Ford", model = "Mustang", year = 1964)
lists = []
set_temp = set()

# assignment 01
print("Assignment 01:")
for i in range(10):
  print(i+1, end=' ')

# assignment 02
print("\n\nAssignment 02:")
for i in car:
  print(i, "=", car[i])

# assignment 03
print("\nAssignment 03:")
for i in range(10):
  list = [random.randint(1, 3) for x in range(3)]
  lists.append(list)

for list in lists:
  if tuple(list) in set_temp:
    print(list, end=' ')
    print("exists more than 1 time")
  else:
    set_temp.add(tuple(lists[i]))

# assignment 04
print("\nAssignment 04:")
def merge(*x, **y):
  length = min(len(x), len(y))
  key_lists = tuple(y.keys())
  for i in range(length):
    key = key_lists[i]
    print(x[i], "=", y[key])
      
merge('a', 'b', 'c', a='A', b='B')