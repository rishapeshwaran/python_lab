# create dictionary using {}
dict1 = {
    "rollno" : 2024179039,
    "name" : "rishi"
}
print(dict1)

# create dictonary using dict()
dict2 = dict(color="red",fruit="apple")
print(dict2)

# create dictionary of tuples
dict3 = dict([("name","rishi"),("department","IT"),])
print(dict3)

# member operations in and not in
print("name" in dict3)
print("age" in dict3)
print("name" not in dict3)
print("age" not in dict3)

# add element to dictionary
dict3["college"] = "CEG"
print(dict3)

# remove element to a dictionary `del`
del dict3["college"]
print(dict3)

# coping the element of the dictionary
copyDict = dict3.copy()
print(copyDict)

# nested dictionary
nested_dictionary = {
    "name" : "rishi",
    "rollno" : 2024179039,
    "marks" : {
        "tamil":87,
        "english":60,
        "maths":50
    }
}
print(nested_dictionary)

# looping over keys
print("looping over keys")
for key in nested_dictionary.keys():
    print(key)

# looping over values
print("looping over values")
for value in nested_dictionary.values():
    print(value)

# looping over key item
print("looping over key and values")
for key,value in nested_dictionary.items():
    print(f"{key} : {value}")