generation = input('What generation would you like to know about? ')

match generation:
    case 'Silent Generation':
        print('born before 1945')
    case 'Baby Boomer':
        print('born between 1945 and 1963')
    case 'Generation X':
        print('born between 1964 and 1978')
    case 'Millennial':
        print('born between 1979 and 1993')
    case 'Generation Z':
        print('born between 1994 and 2011')
    case 'Generation Alpha"':
        print('born after 2011')
    case _:
        print('I have no information on ' + generation)
