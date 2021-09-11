# #funk 1
# import random
# def power3(a):
#     return a*a*a
# a = random.randrange(-10,10)
# b = power3(a)
# print(a)
# print(b)

#funk2
import random
# def power234(a,b):
#     b[0]=a*a
#     b[1]=b[0]*a
#     b[2]=b[1]*a
#     return 
# a = random.randrange(-10,10)
# b = [None]*3
# power234(a,b)
# print(a)
# print(b)

# # funk 3

# import random 
# import math
# def mean(x,y,result):
#     result['amean'] = (x+y)/2
#     result['gmean'] = math.sqrt(x*y)
#     return 
# r = {'amean':None,'gmean':None}
# a = random.randrange(-10,10)
# b = random.randrange(0,10)
# c = random.randrange(0,10)
# d = random.randrange(0,10)
# print(a,b,c,d)
# mean(a,b,r)
# print('amean:',r['amean'])
# print('gmean:',r['gmean'])
# mean(c,d,r)
# print('amean:',r['amean'])
# print('gmean:',r['gmean'])
# mean(a,c,r)
# print('amean:',r['amean'])
# print('gmean:',r['gmean'])
# mean(a,d,r)
# print('amean:',r['amean'])
# print('gmean:',r['gmean'])


# #funk4

# import random 
# import math
# def triangle(a,result):
#     result['p']=3*a
#     result['s']=math.sqrt(3)/4*a*a
#     return
# r = {'p':None,'s':None}
# for i in range(3):
#     a = random.randrange(1,10)
#     print(a)
#     triangle(a,r)
#     print('p=',r['p'])
#     print('s=',r['s'])


#     #funk5
# import random 
# import math
# def rectps(x1,y1,x2,y2,result):
#     a = abs(x1-x2)#1-tomonni hosil qilish
#     b = abs(y1-y2) #2-tomonni hosil qilish
#     print(a)
#     print(b)
#     result['p']=2*(a+b)
#     result['s']=a*b
#     return 

# x1,x2=random.sample(range(-10,10),2)
# y1,y2=random.sample(range(-10,10),2)
# print(x1,x2,y1,y2)
# r = {'p':None,'s':None}#r bu dictionary  
# rectps(x1,y1,x2,y2,r)
# print('p=',r['p'])
# print('s=',r['s'])



# #funk6
# def digitcountsum(k,result):
#     s = str(k)
#     n = len(s)
#     _sum = 0
#     for i in range(n):
#         _sum += int(s[i])
#     result['c']=n
#     result['s']=_sum

# r = {'c':None,'s':None}
# for i in range(5):
#     k = random.randrange(1,10000000)
#     print(k)
#     digitcountsum(k,r)
#     print("qatnashgan sonlar soni:",r['c'])
#     print("qatnashgan sonlar yig'indisi:",r['s'])
#     print()


#funk7

# import random
# import math
# def inverdigits(k):
#     s = str(k['k'])
#     s_new = s[::-1]
#     k['k']=int(s_new)

# r = {'k':None}
# for i in range(5):
#     r['k']=random.randrange(1,100000)
#     print("son:",i+1,":",r['k'])
#     inverdigits(r)
#     print("teskarisi:",r['k'])
#     print()


# #+_______________________________________________________________
# a = str(input("Sonni kiriting : "))

# s = len(a)
# yigindi = 0
# for i in range(s):
#     yigindi += int(a[i])
# print("Siz kiritgan son raqamlari yigindisi: ",yigindi)
# print(f"siz kiritgan son {s} xonali ")    



print('salom ')




# x = 5
# y = bin(x)
# print (y)
