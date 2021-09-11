
# class krasovka:
#     def __init__(self,firma,narx,razmer,rangi):
#         self.firma = firma
#         self.narx = narx
#         self.razmer = razmer
#         self.rangi = rangi
#     def __str__(self):
#         return "firma: "+self.firma+"narx: "+self.narx+"razmer: "+self.razmer+"rangi: "+self.rangi

# krasovkalist = []
# while True:
#     print(" + -  yangi krasovka qo'shish\n k -  krasovkalar ro'yxati\n r - razmer bo'yicha sarterovka qilish\n n - narx bo'yicha sarterovka qilish\n q - dasturdan chiqish ")
#     cmd = input("Kamandani kiriting: ")
#     if cmd == "+":
#         firma = input("Firma nomini kiriting: ")
#         narx = input("Krasovka narxini kiriting: ")
#         razmer = input("Razmerini kiriting: ")
#         rangi = input("Rangini kiriting: ")
#         kr = krasovka(firma, narx, razmer,rangi)
#         krasovkalist.append(kr)
#     elif cmd == "k":
#         print("_____________________Krasovkalar royxati___________________")

#         for krasovkalar in krasovkalist:
#             print (krasovkalar)
#     elif cmd == "r":
#          sorted = krasovkalist
#          sorted.sort(key=lambda x: x.razmer)
#          for krasovkalar in sorted:
#              print (krasovkalar)
#     elif cmd == "n":
#         sorted = krasovkalist
#         sorted.sort(key=lambda x: x.narx)
#         for krasovkalar in sorted:
#             print (krasovkalar)
#     elif cmd == "q":
#         break  

#     +++++++++++++++++++++++++++++++___________________________________________________________________________________      




# class phone:
#     def __init__(self,model,marka,narx,yil,rang):
#        self.model = model
#        self.marka = marka
#        self.narx = narx
#        self.yil = yil
#        self.rang = rang
#     def __str__(self):
#        return   "modeli " + self.model + " Markasi " + self.marka + " narxi " + self.narx + " rangi " + self.rang + " yili " + self.yil
# phonelist = []
# while True:
#     print(" + ma'lumot qoshish\n M - model\n $ - narx\n R - rangi \n Royxat - Royxatni korish uchun\n  MR - markasi\n Y - yili\n q - quit ")
#     cmd = input(" buyruqlardan birini tanlang ")
#     if cmd == "+":
#         model = input(" modelni kiriting ")
#         marka = input(" markani kiriting ")
#         narx = input(" narxni kiriting ")
#         rang = input(" rangni kiriting ")
#         yil = input(" yilni kiriting ")
#         st = phone(model, marka, narx, yil, rang)
#         phonelist.append(st)
#     elif cmd == "$":
#         sortedlist = phonelist
#         sortedlist.sort(key=lambda x: x.narx)
#         for phone in sortedlist:
#             print(phone)
#     elif cmd == "Y":
#         sortedlist = phonelist
#         sortedlist.sort(key=lambda x: x.yil)
#         for phone in sortedlist:
#             print(phone)    
#     elif cmd == "Royxat":
#         print("__________Telefonlar_____Royxati________")
#         for phone in phonelist:
#             print(phone)
#         print("__________Telefonlar_____Royxati________")
#     elif cmd == "q":
#         break


a = input('so kiriting ')
b = input('ikkichi soni kiritig')
c = a+b


 