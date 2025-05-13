# Tuple unpacking
stock_prices = [('Apple', 150), ('Google', 120), ('Microsoft', 200), ('Amazon', 180), ('Tesla', 220)]

for com, price in stock_prices:
    print(f"{com} value {price}")

print('\nAll stock incresed by 10%\n')

for com, price in stock_prices:
    print(f"{com} value {1.1*price:.1f}")


work_hours = [('Abby', 10000), ('John', 150), ('Alice', 120), ('Bob', 90)]
# find employee of the month by comparing the work hours

def person_work_most(wl):
    current_max = 0
    current_star = ''
    for name, hours in work_hours:
        if hours > current_max:
            current_max = hours
            current_star = name
        else:
            pass
    return (current_star,current_max)

name, work_hours = person_work_most(work_hours)
print(f'{name} worked for {work_hours} hours!!\nEmployee of the month')
