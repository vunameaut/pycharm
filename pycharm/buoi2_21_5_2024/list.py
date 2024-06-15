li = list(input("nhap 1 danh sach").split())
print (li)


add = input("add phân tử")
li.append(add)
print (li)
li.clear()

sua = input("sua phần tử")
li.index(sua)
print (li)
li.clear()

print("sap xep")
sapxep=li.sort()
print (sapxep)
li.clear()

remove = input("clear phần tử :")
li.remove(remove)
print (li)
li.clear()