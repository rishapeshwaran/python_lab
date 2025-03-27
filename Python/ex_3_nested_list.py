matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix)

print("insert")
matrix.insert(3,[11,12,13])
print(matrix)

matrix[3].insert(0,10)
print(matrix)

print("deleting")
del matrix[3][3]
print(matrix)
del matrix[3]
print(matrix)

print("reverse")
matrix.reverse()
print(matrix)
matrix[0].reverse()
print(matrix)

print("for loop iteration")
for outer in matrix:
    for inner in outer:
        print(inner)

print("using ranges")
print(matrix)
print(matrix[::2])
print(matrix[0][2::])

print("enumerate")
print(list(enumerate(matrix)))

for item in matrix:
    print(list(enumerate(item)))