list = [32,34,12,76,21,43,54,34,34]
print("minimun of list")
print(min(list))

print("sum of list")
print(sum(list))

print("max of list")
print(max(list))

print("len of list")
print(len(list))

print("reverse of list")
list.reverse()
print(list)

print("sort of list")
list.sort()
print(list)

print("extend of lists")
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

print("insert of list")
cars.insert(1,"TATA")
print(cars)

print("count 34 in list")
print(list.count(34))


print("append item of list")
cars.append("TESLA")
print(cars)

print("clear in list")
cars.clear()
print(cars)

print("del in list")
print(f"before del {fruits}")
del fruits[4:]
print(f"after del {fruits}")


print("remove in list")
fruits.remove("Ford")
print(f"after remove {fruits}")

print("pop in list")
fruits.pop()
print(f"after pop {fruits}")
