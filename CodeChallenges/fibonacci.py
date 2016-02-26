''' Find the nth of the Fibonacci sequence'''

def fib(n):
	current = 0
	last = 1

	for i in range(n):
		current, last = last, current + last
	return current


print fib(7)
	

		