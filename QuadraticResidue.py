#coding=utf-8
#QuadraticResidue.py
import IntegralDomain

def if_prime(p):
	if (p>1):
		if p==2:
			return True
		else:
			for i in range(2,int(p/2)+1):
				if (p%i==0):
					return False
			return True
	else:	
		return False

def if_odd_prime(p):
	if (p>2):
		for i in range(2,int(p/2)+1):
			if (p%i==0):
				return False
		return True
	else:	
		return False

#p>2
def Legendre_symbol(a,p,odd_prime=False):
	if not odd_prime:
		odd_prime= if_prime(p) and p%2!=0
	if odd_prime:
		a=a%p
		if a%p == 0:
			return 0
		elif a == 2:
			#print('a='+str(a)+',p='+str(p))
			return int((-1)**((p*p-1)/8))
		elif a == 1:
			#print('a='+str(a)+',p='+str(p))
			return 1
		elif a == -1:
			#print('a='+str(a)+',p='+str(p))
			return int(-1**((p-1)/2))
		elif if_odd_prime(a):
			#print('a='+str(a)+',p='+str(p))
			return int(Legendre_symbol(p,a)*pow(-1,(p-1)/2*(a-1)/2))
		else:
			factor=IntegralDomain.factorization(a)
			tmp=1
			for i in factor:
				#print('i='+str(i)+',p='+str(p))
				tmp = tmp * Legendre_symbol(i,p)
			return tmp
	else:
		return False

def Jacobi_symbol(a,m):
	if p % 2 != 1:
		a = a % m
		if a%p == 0:
			return 0
	
	else:
		return False

#QuadraticResidueSolution二次同余式求解
def qrs(a,p):
	#计算勒让德符号
	if Legendre_symbol(a,p)==1:
		#分解p=2^s*t+1
		s=0
		t=p-1
		while t%2==0:
			s=s+1
			t=int(t/2)
		print('s='+str(s)+',t='+str(t))
		#计算一个非平方剩余b
		b=0
		for i in range(2,p):
			if Legendre_symbol(i,p)==-1:
				b=i
				break
		print('b='+str(b))
		#计算A=a^t B=b^t
		A=IntegralDomain.rsmc(a,t,p)
		print('A='+str(A))
		B=IntegralDomain.rsmc(b,t,p)
		print('B='+str(B))
		#C=A k=0
		print('-----------------')
		C=A
		k=0
		#C=1则退出,x=a^(t+1)/2*B^k
		while C != 1:
		#计算C^2^(s-j)=1的最大j 1<=j<=s
			for tmp_j in range(1,s+1):
				if pow(C,pow(2,tmp_j))%p == 1:
					j=s-tmp_j
					print('j='+str(j))
					break
		#C=C*B^2j,k=k+2^j-1
			C=C*pow(B,2*j)%p
			print('C='+str(C))
			k=k+pow(2,j-1)
			print('k='+str(k))
			print('-----------------')
		return int(pow(a,(t+1)/2)*pow(B,k)%p)
	return False