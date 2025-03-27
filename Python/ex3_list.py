world_animals = ['Anaconda', 'platypus', 'red panda', 'beaver', 'killer whale', 'platypus', 'camel', 'polar bear', 'king penguin', 'snow leopard', 'zebra', 'plains bison']
world_biomes = ['tropical rainforest', 'temperate forest', 'taiga', 'marine', 'freshwater', 'desert', 'arctic tundra', 'antarctic tundra', 'alpine tundra', 'tropical grassland', 'temperate grassland']

print(len(world_animals))
print(len(world_biomes))

for item in set(world_animals):
    print(f"{item} {world_animals.count(item)}")

print(f"Merge list is : {world_animals + world_biomes}")

print(f"Index of snow leopard is {world_animals.index("snow leopard")}")

if "platypus" in world_animals:
    print("Platypus is in the list")
else:
    print("Platypus is not in the list")

print("taiga is in the list" if "taiga" in world_biomes else "taiga is not in the list")

world_biomes.reverse()
print(f"Reversed list is {world_biomes}")

# Concatenating the two lists alternately
combined_list = [item for pair in zip(world_animals, world_biomes) for item in pair]

print(combined_list)

world_animals.insert(3,"Elephant")

print("removoed alternative Items")
rem_alternate_list = world_animals[::2]
print(rem_alternate_list)


reversed_world_biomes = world_biomes[::-1]

print("combine list 1 same order list 2 reversed order")
combined_list = [item for pair in zip(world_animals, reversed_world_biomes) for item in pair]

print(combined_list)