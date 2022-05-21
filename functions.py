# unctions in python are used for the compartmentalization of code
def addition(num1, num2):
    return num1 + num2;


print(addition(238, 89))


# positional  arguments: where positioning of the arguments matter

def position(first_name, last_name):
    return first_name + ' ' + last_name

print(position('Jenipher', 'Onyango'))
print(position('Onyango', 'Jenipher'))

# named arguments: the positioning does not matter and thy help improve the readability of the code
print(position(last_name='Onyango', first_name='Jenipher'))