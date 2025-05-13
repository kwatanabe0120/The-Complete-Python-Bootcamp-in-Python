# function to check if the argument is even or odd
def is_even(num):
    return num % 2 == 0

print(is_even(10))


# return true if any number is even inside a list
def is_only_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False    
            

l = [1,3]
print(is_only_even_list(l))

# function to return all the even number in a list
def back_even_list(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

l1 = [1,2,3,43,45,5,6,6,6,7,78,88,8]
l2 = [1,3,5]
print(back_even_list(l2))
