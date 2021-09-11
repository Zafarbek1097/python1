# #o'zgaruvchi bu xotiraning nomlangan qismi
# #int,float, string, list, dict
# a = float(input('Shu yerda qiymat kiriting:'))
# print(a)
# #if shart operatorlari
# b = float(input('2-sonni kiriting:'))
# if a < b:#bu 1-shart 
#     print("a b dan kichik")#shart tanasi
# elif a > b:#bu shart 2
#     print("a b dan katta")
# elif a==b:
#     print("a va b o'zaro teng")
# else:
#     print("uzr biz amalni bajara olmadik")

# # 20-misol
# import random
# import math

# x1, x2 = random.sample(range(1,10),2)
# print ("Biz tanlagan x1 x2  sonlar",x1,x2)

# y1,y2 = random.sample(range(1,10),2)
# print("Biz tanlagan y1 y2  sonlar",y1,y2)

# a = math.sqrt((x2-x1)**2+(y2-y1)**2)
# print("Ikki nuqta orasidagi masofa:",a)

# # 21-misol

# import random
# import math

# x1, x2, x3 = random.sample(range(1,10),3)
# print ("Biz tanlagan x1 x2 x3  sonlar",x1,x2,x3)

# y1,y2,y3 = random.sample(range(1,10),3)
# print("Biz tanlagan y1 y2 y3  sonlar",y1,y2,y3)

# a = math.sqrt((x2-x1)**2+(y2-y1)**2)
# print("a=",a)
# b = math.sqrt((x2-x3)**2+(y2-y3)**2)
# print("b=",b)
# c = math.sqrt((x1-x3)**2+(y1-y3)**2)
# print("c=",c)
# p = a+b+c
# print("p=",p)


# if (a!=b and   b!=c and   c!=a):
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("s=",s)
#     p2 = (a+b+c)/2 #yarim perimetri
#     print("p2=",p2)
# else:
#     print("Tomonlar ustma ust tushdi!")    

# # 22-misol
# import random
# A = random.randrange(10,20)
# B = random.randrange(10,20)
# print("A=",A)
# print("B=",B)

# c=A
# A=B
# B=c

# print("A=",A)
# print("B=",c)

# # 23-misol
# import random
# A = random.randrange(1,10)
# B = random.randrange(10,20)
# C = random.randrange(20,30)
# print("A=",A)
# print("B=",B)
# print("C=",C)

# e = A
# A = C
# C = B
# B = e

# print("A=",A)
# print("B=",B)
# print("C=",C)

# 24 -misol

# import random

# A = random.randrange(1,5)
# B = random.randrange(5,10)
# C = random.randrange(20,30)
# print("A=",A)
# print("B=",B)
# print("C=",C)

# e = B
# B = C
# C = A
# A = e

# print("A=",A)
# print("B=",B)
# print("C=",C)

# 25-misol

# import random
# x = random.randrange(1,10)
# print("x=",x)
# y = 3*x**6-6*x**2-7
# print('Funksiyaning qiymati y=',y )

# # 26-misol

# import random
# x = random.randrange(1,10)
# print("x=",x)
# y = 4*(x-3)**6-7*(x-3)**3+2
# print('Funksiyaning qiymati y=',y )

# # 27-misol

# import random
# A = random.randrange(1,5)
# print("A=",A)
# print(A**2,A**4,A**8)

# 28-misol

# import random
# A = random.randrange(1,5)
# print("A=",A)
# print(A**2,A**3,A**5,A**10,A**15)

# # 29 - misol
# import random
# import math

# a = random.randrange(10,500)
# print("Alfa a=",a)
# if 0<a<360:
#     rad = a*math.pi/180
#     print("rad=",rad)
# else:
#     print("Siz 0 va 360  oralig'idagi son kiritishingiz kerak")

# # 30-misol
# import random
# import math

# a = random.randrange(1,10)
# print("Alfa a=",a)
# if 0<a<2*math.pi:
#     grad = a*180/math.pi

#     print("grad=",grad)
# else:
#     print("Siz 0 va 2pi  oralig'idagi son kiritishingiz kerak")

# 31-misol



























