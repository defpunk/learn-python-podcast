birth_year = int(input('What year were you born in? '))

match birth_year:
    case _ if birth_year < 1945:
        print('Silent Generation')
    case _ if birth_year < 1964:
        print('Baby Boomer')
    case _ if birth_year < 1979:
        print('Generation X')
    case _ if birth_year < 1994:
        print('Millennial')
    case _ if birth_year < 2012:
        print('Generation Z')
    case _:
        print('Generation Alpha')