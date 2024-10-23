birth_year = int(input('What year were you born in? '))

if birth_year < 1945:
    print('Silent Generation')
elif birth_year < 1964:
    print('Baby Boomer')
elif birth_year < 1979:
    print('Generation X')
elif birth_year < 1994:
    print('Millennial')
elif birth_year < 2012:
    print('Generation Z')
else:
    print('Generation Alpha')
