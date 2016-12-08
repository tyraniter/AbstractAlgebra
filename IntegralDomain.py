#coding=utf-8
#IntegralDomain.py

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
	tmp_a=max(a,b)
	tmp_b=min(a,b)
	d=gcd(a,b)
	x=(1,0)
	y=(0,1)
	i=1
	while tmp_b != d:
		q=int(tmp_a/tmp_b)
		x=(x[1],x[0]+x[1]*q)
		y=(y[1],y[0]+y[1]*q)
		(tmp_a,tmp_b) = (tmp_b,tmp_a % tmp_b)
		i=i+1
	return (x[1]*(-1)**i,-y[1]*(-1)**i)
	

#repeat_square_modulus_calculation
def rsmc(b,n,m):
	if not isinstance(b,int) or not isinstance(n,int) or not isinstance(m,int):
		return false
	tmp_a = 1
	tmp_b = b % m
	bin_n=bin(n)[2:]
	for i in range(len(bin_n)-1,-1,-1):
		if bin_n[i] == '1':
			tmp_a=(tmp_a * tmp_b) % m
		tmp_b=(tmp_b * tmp_b) % m
	return tmp_a

def factorization(n):
	if not isinstance(n,int):
		return False
	if n == 0 or n*n == 1:
		return False
	tmp_n=abs(n)
	factor=[]
	for i in range(2,int(tmp_n**0.5)+1):
		while True:
			if tmp_n%i == 0:
				factor.append(i)
				tmp_n=int(tmp_n/i)
			else:
				break
	if tmp_n!=1:
		factor.append(tmp_n)
	return factor