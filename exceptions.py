# exceptions in python is used as a method of imposing fault tolerance
# types of faults/errors that may occur include: value, type, import, index, key, etc
try:
    value = int(input('>>'))
    print(value + 'one')

except ValueError:
    print('This is a value Error')
except TypeError:
    print('this is a type error')
