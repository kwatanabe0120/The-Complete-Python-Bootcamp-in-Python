def new_decorator(originak_func):
    def wrap_func():
        print('\nCode here before the original function!\n')
        originak_func()
        print('\nCode here after the original function!\n')
    return wrap_func

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')

# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()

func_needs_decorator()