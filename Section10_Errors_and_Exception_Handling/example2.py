try:
    # change from w to r to get error
    file = open('test.txt','r')
    file.write('test!')
except OSError:
    print('OSError happens')
except TypeError:
    print('TypeError happens')
finally:
    print('I always run')