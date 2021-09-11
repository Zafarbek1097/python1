class auto:#avtomobillar classi
    def __init__(self,markasi,rusumi,narxi,yili,rangi):
        self.markasi=markasi
        self.rusumi=rusumi
        self.narxi=narxi
        self.yili=yili
        self.rangi=rangi
    def __str__(self):
        return "markasi: "+self.markasi+" rusumi: "+self.rusumi+" narxi: "+self.narxi+" yili: "+self.yili+" rangi: "+self.rangi
autolist=[]
while True:
    print("+marka qo'shish\n t-mashinalar ro'yxati\n r-mashina yili bo'yicha sortirovka\n s-mashina narxi\n y-mashina yili sortirovka\n c-mashina rangi\n q-quit")
    cmd = input("komandani kiriting:")
    if cmd=="+":
        marka = input("markasi:")
        rusum = input("rusumi:")
        narx = input("narxi:")
        yili = input("yili:")
        rang = input("rangi:")
        st=auto(marka,rusum,narx,yili,rang)
        autolist.append(st)
    elif cmd =="t":
        print("____ mashinalar ro'yxati___")
        for auto in autolist:
            print(auto)
        print("____mashinalar rro'yxati___")   
    elif cmd =="r":
        sortedlist = autolist
        sortedlist.sort(key=lambda x:x.yili)
        for auto in sortedlist:
            print(auto)
    elif cmd =="s":
        sortedlist = autolist
        sortedlist.sort(key=lambda x:x.narxi)
        for auto in sortedlist:
            print(auto)
    # elif cmd == "y":
    #     sortedlist = autolist
    #     sortedlist.sort(key=lambda x: x.yili)
    #     for auto in sortedlist:
    #         print(auto)
    # elif cmd == "c":
    #     sortedlist = autolist
    #     sortedlist.sort(key=lambda x: x.rang)
    #     for auto in sortedlist:
    #         print(auto)
    elif cmd == "q":
        break


#uyga vazifa : Sanjarbek kompyuter class: marka , model , narxi, yili
# uyga vazifa: umumiy holatda  sovchi class yaratilsin:
#maydonlari qiz ismi sharifi
#tug'ilgan yili
#bo'yi
