# # polomorfizm - bu classalarni ierarxik maydonlarga yoki metodlarga murojat qiliishi

# class  Duck:
#     def quack(self): print("quack")
#     def walk(self): print("walk like a duck")
#     def bark(self): print("the duck connot duck")
#     def fur(self):  print("the duck has feathers ")

# class Dog:
#     def bark(self): print("woof")
#     def fur(self):  print("the dog has brown and white fur")
#     def walk(self): print("walks like a dog")
#     def quack(self): print("the dog connot quack")

# def main():
#     donald = Duck()
#     fido = Dog()
#     in_the_forest(donald)
#     in_the_pond(fido)

# def in_the_forest(cat):
#     cat.bark()
#     cat.fur()
# def in_the_pond(duck):
#     duck.quack()
#     duck.walk() 

# if __name__== "__main__":main() #funksiyalar nomlari ichida main deb keladigan funksiyalar  mavjud bo'lsa faqat shu ishga tushirilsin




# Decorotorlar - yopiq maydonlarga  kirish huquqini olish

# class Duck:
#     def __init__(self,**kwargs):#  kwargs ko'plab argumentlar # args argumentlar soni cheklangan
#         self.properties = kwargs
#     def  quack(self):
#         print("quack")
#     def walk(self):
#         print("walks like a duck")
#     def get_properties(self):
#         return self.properties
#     def get_property(self,key):
#         return self.properties.get(key,None)

#     @property
#     def color(self):
#         return self.properties.get('color',None)
#     @color.setter
#     def color(self,c):
#         self.properties['color']=c 
#     @color.deleter
#     def color(self):
#         del self.properties['color']
# def main():
#     donald = Duck()
#     donald.color = 'yellow'
#     print (donald.color)

# if __name__ == '__main__':main()            

#class for sikli inclusive   deb yuritiladi

# class inclusive_range:
#     def __init__(self,*args):
#         numargs = len(args)

#         if numargs<1: raise  TypeError("we expect arguments")

#         elif numargs == 1:
#             self.stop  = args[0]
#             self.start = 0
#             self.step = 1
#         elif numargs == 2:
#             (self.start,self.stop) = args
#             self.step = 1
#         elif numargs == 3:
#             (self.start,self.stop,self.step) = args

#         else:
#             raise  TypeError("Excepted at most 3 arguments, got{} ".format(numargs))
#     def __iter__(self):
#         i = self.start
#         while i <= self.stop:
#             yield i
#             i+= self.step
# def main():
#     o = inclusive_range(1,20,1)
#     for i in o: print(i)
# if __name__ == '__main__':main()    

o = list(range(1,20,1))
for i in o: print(i,)








