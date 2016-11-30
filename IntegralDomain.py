#coding=utf-8

#a>b>0
def euclidean_division(a,b):
	if a == 0 or b == 0:
		return False
	return (b,a%b)

'''def print_euclidean_division(a,b):
	print(str(a)+'='+str(b)+'*'+str(a/b)+'+'+str(a%b))'''

def if_prime(p):
	if not isinstance(p,int):
		return False
	if p == 0 or p*p == 1:
		return False
	tmp_p=abs(p)
	'''if tmp_p == 2 or tmp_p == 3:
		return True'''
	for i in range(2,int(tmp_p**0.5)+1):
		if p%i == 0:
			return False
	return True

def gcd(a,b):
	if not isinstance(a,int) or not isinstance(b,int):
		return False
	if a == 0 or b == 0:
		return abs(a+b)
	tmp_a=max(abs(a),abs(b))
	tmp_b=min(abs(a),abs(b))
	while tmp_b != 0:
		(tmp_a,tmp_b)=euclidean_division(tmp_a,tmp_b)
	return tmp_a

def lcm(a,b):
	if not isinstance(a,int) or not isinstance(b,int):
		return False
	if a == 0 or b == 0:
		return 0
	return int(abs(a*b)/gcd(a,b))

#x=x0+k*b/d,y=y0-k*a/d
def bezout_identity(a,b):
	if not isinstance(a,int) or not isinstance(b,int):
		return False
	d=gcd(a,b)


