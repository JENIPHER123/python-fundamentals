# conditional statements are used to execute one statement if a condition is true and another when the condidtion is
# false

pg1 = input('Is the movie a pg movie: y=yes and n=no').lower()
age1 = int(input('How old are you: '))

pg_movie = pg1
age = age1

if pg1 == 'y' and age1 < 18:
    print('you are not allowed to watch this movie')
elif pg1 == 'n':
    print('you can watch the movie')

# logical operators include AND OR and NOT

music = True
art = False
dance = True

if music and dance:
    print('music and dance')
elif music or art:
    print('music or art')
elif music or not dance:
    print('music or not dance')

# comparison operators: < > = ==
if age1 == 18:
    print('you are a young adult')
elif age1 > 18:
    print('you are an older adult')
elif age1 < 18:
    print('you are a child')
