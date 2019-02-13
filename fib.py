"""
a, b, c
0, 1, 1, 2, 3, 5, 8, 13 ......
   a, b


0, 1, 1
"""

def fib(n):
	a = 0
	b = 1
	print(a)
	print(b)
	for i in range(n):
		c = a + b
		print(c)
		a = b
		b = c
		

print(fib(10))