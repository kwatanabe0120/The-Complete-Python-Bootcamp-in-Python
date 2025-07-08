import time

def func_one(n):
	return [str(num) for num in range(n)]

def func_two(n):
	return list(map(str, range(n)))


start_time = time.time()
func_one(100000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)


start_time = time.time()
func_two(100000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

