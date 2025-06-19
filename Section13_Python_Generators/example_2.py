def get_fibon(n):
	a = 1
	b = 1
	for _ in range(n):
		yield a
		a,b = b,a+b


for number in get_fibon(5):
	print(number)