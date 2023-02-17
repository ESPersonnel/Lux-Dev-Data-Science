# List Methods
# append() - Adds an element to the end of a list
# extend() - Adds all the elements of another list to the end of a list
# insert() - Inserts an element at a specified index
# remove() - Removes the first occurrence of an element from a list
# pop() - Removes and returns an element at a specified index
# index() - Returns the index of the first occurrence of an element in a list
# count() - Returns the number of times an element appears in a list
# sort() - Sorts the elements of a list in ascending order
# reverse() - Reverses the order of the elements in a list
# Tuple Methods
# count() - Returns the number of times an element appears in a tuple
# index() - Returns the index of the first occurrence of an element in a tuple
# Set Methods
# add() - Adds an element to a set
# update() - Adds all the elements of another set to a set
# remove() - Removes an element from a set; raises an error if the element is not in the set
# discard() - Removes an element from a set if it is present
# pop() - Removes and returns an arbitrary element from a set
# clear() - Removes all the elements from a set
# Dictionary Methods
# keys() - Returns a list of the keys in a dictionary
# values() - Returns a list of the values in a dictionary
# items() - Returns a list of the key-value pairs in a dictionary
# get() - Returns the value for a given key; if the key is not found, returns a default value (or None if not specified)
# update() - Updates a dictionary with the key-value pairs from another dictionary
# pop() - Removes and returns the value for a given key; raises an error if the key is not found
# popitem() - Removes and returns an arbitrary key-value pair from a dictionary

# Code

# List Methods
# append()
x = [1, 2, 3]
x.append(4)
print(x) # [1, 2, 3, 4]

# extend()
x = [1, 2, 3]
x.extend([4, 5])
print(x) # [1, 2, 3, 4, 5]

# insert()
x = [1, 2, 3]
x.insert(0, 0)
print(x) # [0, 1, 2, 3]

# remove()
x = [1, 2, 3]
x.remove(2)
print(x) # [1, 3]

# pop()
x = [1, 2, 3]
x.pop(0)
print(x) # [2, 3]

# index()
x = [1, 2, 3]
print(x.index(2)) # 1

# count()
x = [1, 2, 3, 1]
print(x.count(1)) # 2

# sort()
x = [1, 2, 3, 1]
x.sort()
print(x) # [1, 1, 2, 3]

# reverse()
x = [1, 2, 3, 1]
x.reverse()
print(x) # [1, 3, 2, 1]

# Tuple Methods
# count()
x = (1, 2, 3, 1)
print(x.count(1)) # 2

# index()
x = (1, 2, 3, 1)
print(x.index(2)) # 1

# Set Methods
# add()
x = {1, 2, 3}
x.add(4)
print(x) # {1, 2, 3, 4}

# update()
x = {1, 2, 3}
x.update([4, 5])
print(x) # {1, 2, 3, 4, 5}

# remove()
x = {1, 2, 3}
x.remove(2)
print(x) # {1, 3}

# discard()
x = {1, 2, 3}
x.discard(2)
print(x) # {1, 3}

# pop()
x = {1, 2, 3}
x.pop()
print(x) # {2, 3}

# clear()
x = {1, 2, 3}
x.clear()
print(x) # set()

# Dictionary Methods
# keys()
x = {'a': 1, 'b': 2}
print(x.keys()) # dict_keys(['a', 'b'])

# values()
x = {'a': 1, 'b': 2}
print(x.values()) # dict_values([1, 2])

# items()
x = {'a': 1, 'b': 2}
print(x.items()) # dict_items([('a', 1), ('b', 2)])

# get()
x = {'a': 1, 'b': 2}
print(x.get('a')) # 1

# update()
x = {'a': 1, 'b': 2}
x.update({'c': 3})
print(x) # {'a': 1, 'b': 2, 'c': 3}

# pop()
x = {'a': 1, 'b': 2}
x.pop('a')
print(x) # {'b': 2}

# popitem()
x = {'a': 1, 'b': 2}
x.popitem()
print(x) # {'a': 1}

