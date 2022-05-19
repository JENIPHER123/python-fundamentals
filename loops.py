# while loop demonstration using while loops
guess = input('>> Guess: ')
number= 1
while number < 3:
    if guess == '12':
        print('You win!!')
        break
    else:
        guess = input('>> Guess: ')
        number = number + 1
        if number >= 3:
            print('you lost!!')
            break

# for loop demonstration with shopping cart items and pricing calculations
items_in_shopping_cart = [12, 348, 123, 456, 19, 990]
total=0

for item in items_in_shopping_cart:
    total = total + item

print(total)

# nested loop demonstration using for loop
for i in range(4):
    for r in range(4):
        print(i , r)
