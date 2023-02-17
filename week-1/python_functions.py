# Code

# Function
def hello():
    print('Hello World!')

hello()

# Function with Parameters
def hello(name):
    print('Hello ' + name)

hello('John')

# Function with Return Value
def add(x, y):
    return x + y

print(add(1, 2))

# Function with Default Parameter
def hello(name = 'John'):
    print('Hello ' + name)

hello()

# Function with Variable Number of Parameters
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))

# Function with Keyword Arguments
def hello(**kwargs):
    print('Hello ' + kwargs['name'])

hello(name = 'John')

# Function with Variable Number of Keyword Arguments
def hello(**kwargs):
    print('Hello ' + kwargs['name'])

hello(name = 'John', age = 30)

  