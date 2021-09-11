#class -  sinf 
#class ning mazmuni real obyektni koddagi nusxasi
#class auto:

class Student:#talaba sinfi 
    def __init__(self,fish,crs,ball):
        self.fish = fish
        self.crs = crs
        self.ball = ball
    def __str__(self):
        return "FISH:" + self.fish+" Kurs: "+self.crs+" Baho: "+self.ball

studentlist = []#bo'sh holatda massiv e'lon qilamiz
while True: #qachon break to'xtatish komandasi berilguncha kod ishlasin
    print("+ talaba qo'shish\n t - talabalar ro'yxati\n s - talabalarni bahosi asosida tartiblash \n k - talaba kursi asosida sortirovka\nq - quit ")
    cmd = input("komandani kiriting:")
    if cmd == "+":
        fish = input("FISH:")
        crs = input("Kursi:")
        ball = input("Bahosi:")
        st = Student(fish,crs,ball)
        studentlist.append(st)
    elif cmd == "t":
        print("_____________Talabalar ro'yxati______________")
        for student in studentlist:
            print(student)
        print("_____________Talabalar ro'yxati______________")
    elif cmd == "s":
        sortedlist = studentlist
        sortedlist.sort(key=lambda x: x.ball)
        for student in sortedlist:
            print(student)
    elif cmd == "k":
        sortedlist = studentlist
        sortedlist.sort(key=lambda x: x.crs)
        for student in sortedlist:
            print(student)
    elif cmd == "q":
        break


