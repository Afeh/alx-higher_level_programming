def fib(n):
	"""Returns a list containing the fibonacci series up to n."""
	result = []
	a, b = 0, 1 
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

f = fib(100)

print(f)