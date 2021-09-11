# # print('salom')
# # print("hello world")
# # 2-misol kvadrat tomoni berilgan uning yuzasi aniqlansin
# a = float(input('kvadrat tomoni kiritilsin:'))

# s = a*a
# print("Kvadrat yuzasi:",s)


# # 4-misol 
# pi = 3.14
# d = float(input('Diametrni kiriting:'))
# l = pi * d
# print("Aylana uzunligi:",l)


# 6-misol
# import random
# a = random.randrange(1,10)
# b = random.randrange(1,10)
# c = random.randrange(1,10)
# print(a,b,c)
# v = a * b * c 
# print("Hajm:",v)
# s = 2*(a*b+b*c+a*c)
# print("To'la sirti:",s)


# #8-misol
# import random 
# a = random.randrange(1,10)
# b = random.randrange(1,10)
# print(a,b)
# ariphmetic = (a+b)/2
# print(ariphmetic)


# #9-misol
# import random 
# import math
# a = random.randrange(1,10)
# b = random.randrange(1,10)
# print(a,b)
# geometric = math.sqrt(a*b)
# print(geometric)
#____________________________________amaliy mashg'ulot___________++++++++++++++++++++++_________________________________________________________________________________

# 1-2-misol

# import random

# a = random.randrange(1,10)
# print("berilgan a sonimiz",a," ga teng")
# p = 4*a
# s = a**2
# print('kvadratning peremetri ',p,' ga teng')
# print('kvadratning yuzi ',s,' ga teng')

# 3-misol

# import random
# a = random.randrange(1,20)
# b = random.randrange(1,30)
# print('Berilgan a sonimiz ',a,' ga teng\nBerilgan b sonimiz ',b,' ga teng ')
# p = 2*(a+b)
# s = a*b
# print('To\'rtburchakni peremetri ',p,' ga teng')
# print('To\'rtburchakni yuzi ',s,' ga teng')

# # 4-misol
# import random
# import math
# d = random.randrange(1,20)
# print('Aylananing diametri ',d,' ga teng')
# l = d*math.pi
# print('Aylananing uzunligi ',l,' ga teng')

# # 5-misol
# import random
# a = random.randrange(5,15)
# print('Kubning tomoni ',a)
# v = a**3
# s = 6*a**2
# print('Kubning hajmi',v)
# print('Kubning to\'la sirti',s)

# # 6-misol

# import random
# a = random.randrange(1,5)
# b = random.randrange(5,10)
# c = random.randrange(10,15)

# print('Parallelipidning tomonlari ',a,b,c)
# v = a*b*c
# s = 2*(a*b+b*c+a*c)
# print('Parallelipidning hajmi',v)
# print('Parallelipidning to\'la sirti',s)

## 7-misol
# import random
# import math
# r = random.randrange(1,10)
# print('Doira radiusi',r)
# l = 2*math.pi*r
# s = math.pi*r**2
# print('Doira uzunligi',l)
# print('Doira yuzi',s)

# # 8-misol
# import random
# a = random.randrange(1,5)
# b = random.randrange(5,10)
# print('Berilgan son',a,b)
# c = (a+b)/2
# print('Berilgan sonlarning o\'rta arifmetigi',c)

# 9-misol

# import random
# import math

# a = random.randrange(1,5)
# b = random.randrange(5,10)
# print('Berilgan son',a,b)
# c = math.sqrt(a*b)
# print('Berilgan sonlarning o\'rta geometrigi',c)

# 10-11-misollar

# import random
# import math

# a = random.randrange(1,10)
# b = random.randrange(1,10)
# print('Berilgan son',a,b)
# yig = a+b
# kop = a*b
# kv = a**2
# kv2 = b**2
# mod = abs(a)
# mod2 = abs(b)
# print('Yig\'indisi',yig,'\nkopaytmasi',kop,'\n1-son kvadrati',kv,'\n2-son kvadrati',kv2,'\n1-son moduli',mod,'\n2-son moduli',mod2)

# 12-misol

# import random
# import math

# a = random.randrange(1,20)
# b = random.randrange(1,20)
# print('Uchburchak katetlari',a,b)

# c = math.sqrt(a*a+b*b)
# p = a+b+c
# print('Uchburchakning c tomoni',c,'\nUchburchakning perimetiri',p)

# 13-misol
# import random
# import math

# r1, r2 = random.sample(range(1,10),2)
# if r1>r2:
#     print ('r1 va r2 ',r1,r2)
#     s1 = math.pi*r1
#     s2 = math.pi*r2
#     s3 = math.pi*(r1-r2)
#     print('s3=',s3,'ga teng')
# else:
#    print('r1 va r2 ',r1,r2)

# 17-misol

# import random

# a,b,c = sorted(random.sample(range(1,10),3))
# print('a,b,c sonlar',a,b,c)
# ac = c - a
# bc = c - b
# yigindi = ac + bc
# print('Kesmalar uzunligi ',ac,bc)
# print('Yigindisi',yigindi)

# 18-misol

import random

a,c,b = sorted(random.sample(range(1,10),3))
print('a,c,b sonlar',a,c,b)
ac = c - a
bc = b - c
print('Kesmalar uzunligi ',ac,bc)
print('Kesmalar uzunligi ko\'paytmasi= ',ac*bc)





















