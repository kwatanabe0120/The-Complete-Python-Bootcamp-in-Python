while True:
    try:
        result = int(input('Please enter number: '))
    except:
        print('Error happens, try again')
    else:
        print('Thank you!')
        break
    finally:
        print('I run always')