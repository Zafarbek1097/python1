# 1-misol
import random  # if else ga doir misollar
import math# shart operatorlari

# a = random.randrange(-10,10)
# print(a)
# if a>0:
#     print(a+1)
 
#  # 2- misol
# import random  # if else ga doir misollar
# import math# shart operatorlari

# a = random.randrange(-10,10)
# print(a)
# if a>0:
#     print(a+1)
# else:
#     print(a-2)  

# 3-misol

# import random  # if else ga doir misollar
# import math# shart operatorlari

# a = random.randrange(-10,10)
# print(a)
# if a>0:
#     print(a+1)
# elif a==0:
#     print(10)
# else:
#     print(a-2)           

# 4-5-misol

# import random  # if else ga doir misollar
# import math# shart operatorlari

# a = random.randrange(-10,10)
# b = random.randrange(-10,10)
# c = random.randrange(-10,10)
# print(a,b,c)
# x=0
# if a>0:
#     x+=1
# if  b>0:
#     x+=1
# if c>0:
#     x+=1

# print("no'ldan katta sonlar",x)

# y=0
# if a<0:
#     y+=1
# if  b<0:
#     y+=1
# if c<0:
#     y+=1

# print("no'ldan kichik sonlar",y)

# 6-misol

# import random  # if else ga doir misollar
# import math# shart operatorlari

# a = random.randrange(-10,10)
# b = random.randrange(-10,10)
# print(a,b)
# if a>b:
#     print(a)
# else:
#     print(b)

# 7-misol

# import random  # if else ga doir misollar
# import math# shart operatorlari

# a = random.randrange(-10,10)
# b = random.randrange(-10,10)
# print(a,b)
# x=0
# if a>b:
#     x+=1
    
# else:
#     x+=2
# print(x)


#9-misol

# import random
# a= random.randrange(-10,10)
# b= random.randrange(-10,10)
# print(a,b)

# if a<b:
#     print(a,b)
# elif a==b:
#     print("qiymatlar teng")    
# else:
#     a,b = b,a
#     print(a,b) 

# # 10 -misol
# import random
# a= random.randrange(1,10)
# b= random.randrange(1,10)
# print(a,b) 

# if a==b:
#     a,b = 0,0
#     print(a,b)
# else:
#     print(a+b)    

# 12-misol kichigini aniqlovchi dastur
# import random
# a,b,c= random.sample(range(10,50),3)
# print(a,b,c)
# print(min(a,b,a))

# #  13 - misol uchta sonning   o'rtachasini topish

# import random
# a,b,c= random.sample(range(10,50),3)
# print(a,b,c)

# if (a<=b and b<=c) or (c<=b and b<=a):
#     print(b)

# elif (b<=a and a<=c) or (c<=a and a<=b):
#     print(a)

# else:
#      print(c)   


# 14-misol

# import random
# a,b,c= random.sample(range(10,50),3)
# print(a,b,c)

# print(min(a,b,c))
# print(max(a,b,c))

# 15 - misol

# import random
# a,b,c= random.sample(range(1,30),3)
# print(a,b,c)

# if (a<=b and a<=c):
#         print(b+c)

# elif (b<=a and b<=c):
#     print(a+c)

# else:
#      print(a+b) 

  # 16- misol
  
# import random
# a,b,c= random.sample(range(1,30),3)
# print(a,b,c)

# if a<=b and b<=c:
#     print((2*a,2*b,2*c))
# else:
#     print((-a,-b,-c))

  #  17-misol

# import random
# a,b,c= random.sample(range(1,30),3)
# print(a,b,c)

# if (a<=b and b<=c) or (a>=b and b>=c):
#     print((2*a,2*b,2*c))
# else:
#     print((-a,-b,-c))  

#18-misol

# import random
# a= int(input("1-sonni kiriting "))
# b= int(input("1-sonni kiriting "))
# c= int(input("1-sonni kiriting "))
# print(a,b,c)
# x=0
# if a==b:
#     x+=3
# if b==c:
#     x+=1
# if a==c:
#     x+=2

# print (x)     


# 19-misol

# a= int(input("1-sonni kiriting "))
# b= int(input("1-sonni kiriting "))
# c= int(input("1-sonni kiriting "))
# d= int(input("1-sonni kiriting "))

# print(a,b,c,d)
# x=0
# if a==b==c:
#     x+=4
# if a==b==d:
#     x+=3
# if a==c==d:
#     x+=2
# if b==c==d:
#     x+=1
# print (x)        

# 20-misol

# import random

# a = random.randrange(1,20)
# b = random.randrange(1,20)
# c = random.randrange(1,20)
# print(a,b,c)


# e= abs(a-b)
# s=abs(a-c)
# if e<s:
#     print("b nuqta yaqin: ",e)
# else:
#     print("c  nuqta yaqin: ", s)    

# # 21-misol
# import random

# x,y = random.sample(range(-10,10),2)
# print(x,y)
# n=0
# if (x==0 and y==0):
#    n=0
# elif (x==0 and y!=0):
#     n+=1  
# elif (x!=0 and y==0):
#     n+=2
# else:
#     n+=3        

# print (n)

# # 22-misol
# import random

# x,y = random.sample(range(-10,10),2)
# print(x,y)

# if x>0 and y>0:
#     print(' 1-chorak')
# elif x>0 and y<0:
#     print("2-chorak")    
# elif x<0 and y<0:
#     print("3-chorak")
# elif x<0 and y>0:
#     print('4-chorak')    


# 23-misol

# import  random

# x1,x2,x3 = random.sample(range(-10,10),3)
# y1,y2,y3 = random.sample(range(-10,10),3)

# print (x1,x2,x3)
# print (y1,y2,y3)

# # 24-misol

# import random
# import math

# x = random.randrange(-20,20)
# print(x)
# if x>0:
#     f = 2*math.sin(x)
# if x<=0:
#     f = x-6    
# print (f)


# # 25-misol

# import random
# import math

# x = random.randrange(-20,20)
# print(x)
# if x<-2 or x>2:
#     f = x*2
# else:
#     f = -3*x
# print(f)       
   
 # 26-misol

# import random
# import math

# x = random.randrange(-20,20)
# print(x)

# if x>=0:
#     f = -x
# elif x>0 and x<2:
#     f=x*x
# elif x>=2:
#     f = x
# print(f)            
  
# # 29-misol

# import random

# a = random.randrange(-100,100)

# print(a)

# if a>0 and a%2==1:
#     print("Bu son musbat toq son")
# elif a<0 and a%2==0:
#     print("Bu son manfiy juft son")
# elif a==0:
#     print(" Son no'lga teng")
# elif a<0 and a%2==1:
#     print("Manfiy toq son")     
# else:
#   print("Musbat juft son")   

# #30-misol
# import random

# a = random.randrange(1,999)

# x = len(str(a))

# print(a)
# print(x)

# if a%2==0 and x==2:
#       print("Ikki xonali juft son ")
# elif a%2==1 and x==2:
#           print("Ikki xonali toq son ")
# elif a%2==1 and x==3:
#       print("Uch xonali toq son")
# elif a%2==0 and x==3:
#       print("Uch xonali juft son")      
# else:
#   print("Bir xonali son")        
