f=open ("item.txt","w")
itemleft1=500
itemleft2=360
itemleft3=25
itemleft4=320
itemleft5=3
f.write(str(itemleft1)+'\n')
f.write(str(itemleft2)+'\n')
f.write(str(itemleft3)+'\n')
f.write(str(itemleft4)+'\n')
f.write(str(itemleft5)+'\n')
f.close()
file = open('item.txt', 'r')
line = file.readlines()
file.close()