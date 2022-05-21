# dictionaries in pythin help in the translation of input and/or other data to another
phone = input('Enter Pnone Number')

converters = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
}
output = ""
for i in phone:
    output += converters.get(i) + " "

print(output)