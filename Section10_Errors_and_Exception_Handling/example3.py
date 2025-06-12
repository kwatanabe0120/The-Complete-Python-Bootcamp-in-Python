while True:
    try:
        result = int(input('Please enter number: '))
    except ValueError:
        print('Error happens, try again')
    else:
        print('Thank you!')
        break
    finally:
        print('I run always')