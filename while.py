

# Sardor Abdulxamidov, [03.08.21 18:35]
# #while 1
# import random 
# a = random.randrange(50,100)#60
# b = random.randrange(1,a)#1 ...60 #16
# print(a,b)
# r = a - b#60-16 = 44 - 16 = 28 - 16 = 12
# while r>=b:
#     r-=b
# print("qoldiq qismi:",r)

# Sardor Abdulxamidov, [03.08.21 18:39]
# #while 2
# import random 
# a = random.randrange(50,100)#60
# b = random.randrange(1,a)#1 ...60 #16
# print(a,b)
# r = a - b#60-16 = 44 - 16 = 28 - 16 = 12
# n = 1
# while r>=b:
#     r-=b
#     n+=1
# print("qoldiq qismi:",r)
# print("amallar soni:",n)

# Sardor Abdulxamidov, [03.08.21 18:44]
# #while 3
# import random 
# a = random.randrange(1,100)#60 n
# b = random.randrange(1,100)# k
# print(a,b)
# r = a#60-16 = 44 - 16 = 28 - 16 = 12
# n = 0
# while r>=b:
#     r-=b
#     n+=1
# print("qoldiq qismi:",r)
# print("amallar soni:",n)

# Sardor Abdulxamidov, [03.08.21 18:54]
# #while 5
# import random
# k = random.randrange(1,30)
# n = 2**k
# print(k,n)
# k_new = 0
# while n>=2:
#     n/=2
#     k_new += 1
# print("daraja:",k_new)

# Sardor Abdulxamidov, [03.08.21 19:04]
# #while 6
# import random
# n = random.randrange(1,20)
# print(n)
# if n%2==0:
#     l = 2
# else:
#     l = 1
# print(l)
# f = 1
# while n>=l:
#     f*=n
#     n -= 2
# print("2lik faktorial:",f)

# Sardor Abdulxamidov, [03.08.21 19:12]
# #while 7
# import random
# n = random.randrange(1,1000)
# print(n)
# k = 1
# while k*k <= n:
#     k+=1
# print("k={0},k*2={1},(k-1)*2={2}".format(k,k**2,(k-1)**2))

# Sardor Abdulxamidov, [03.08.21 19:33]
# #while 8
# import random
# n = random.randrange(1,1000)
# print(n)
# k = 1
# while k*k<=n:
#     k += 1
# k -= 1
# print("k={0},k*2={1},(k+1)*2={2}".format(k,k**2,(k+1)**2))#formatlash -  ya'ni terminalga chop etish paytida  
# print(k,k**2,(k+1)**2)
# print(k**2)
# print((k+1)**2)

# Sardor Abdulxamidov, [03.08.21 19:39]
# #while 9-10
# import random
# n = random.randrange(2,1000)
# print(n)
# k = 0
# p = 1
# while p<=n:
#     p *= 3
#     k += 1
# k -= 1
# print("k={0},3*k={1},3(k-1)={2}".format(k,3**k,3**(k+1)))