for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print('Error happens')


print('-----------------------------')


try:
    x = 5
    y = 0
    z = x / y
except:
    print('Error happens')
finally:
    print('All done')

print('-----------------------------')

def ask():
    while True:
        try:
            result = int(input('Enter num: '))
            print(result**2)
        except:
            print('Error')
        else:
            break


ask()
