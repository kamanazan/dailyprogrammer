from sys import argv

n = int(argv[1])

#math solution
print n - (((n / 3)) + ((n / 100) ) + ((n / 14) + (n / 42)))
#'programmer' solution
operational = n
for x in range(1, (n+1)):
	if (x % 3 == 0) or (x % 14 == 0) or (x % 100 == 0):
		operational -= 1

print operational

