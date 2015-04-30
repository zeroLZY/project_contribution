#encoding=utf-8
#**Sieve of Eratosthenes** - 
#The sieve of Eratosthenes is one of the most efficient ways 
#to find all of the smaller primes (below 10 million or so).

#就是去掉倍数的那个程序
from math import sqrt

def find_prime(n):
	sqrt_n = int(sqrt(n))
	no_prime = [j for i in range(2,sqrt_n) for j in range(i*2,n,i)]
	prime    = [i for i in range(2,n) if i not in no_prime]
	return prime

print find_prime(100)
print len(find_prime(100))
