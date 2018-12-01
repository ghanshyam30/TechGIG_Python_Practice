##################### Factorial Normal #########################
'''
def fact(n):
     if n==1:
             return 0
     elif n==2:
             return 1
     else:
             return fact(n-1)+fact(n-2)
for n in range(1,6):
	print "{0}:{1}".format(n,fact(n))
'''

#---------------------Factorial with Cache ----------------------
cache_dict={}
def fact(n):
	if n in cache_dict:
		return cache_dict[n]
	if n==1:		
		return 0
	elif n==2:
        	return 1
	else:
		cache_dict[n]=fact(n-1)+fact(n-2)
		return cache_dict[n]
for n in range(1,200):
	print "{0}:{1}".format(n,fact(n))
