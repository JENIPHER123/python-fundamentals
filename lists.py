# lists in python are useful in storing common data
# lists don't necessarily have to have the same datatypes

one = ['Tevin', 45, 1234.94]

# finding largest number in a list
numbers = [12, 3, 45, 90, 112, 41, 23, 67]
largest = 0
for number in numbers:
    if largest < number:
        largest = number

print(largest)

# list functions and properties
# sorting
numbers.sort()
print(numbers)
# remove number
print(numbers.pop(4))
print(numbers)
# add number
numbers.append(344)
print(numbers)


# listing all uniques in a list
mains = [2, 2, 1, 3, 45, 6, 7, 7, 45]
uniques = []

for item in mains:
    if item not in uniques:
        uniques.append(item)
print(uniques)
