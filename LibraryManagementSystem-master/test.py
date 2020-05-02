def check():
    flag=False
    f=open('sample.txt','r')
    lines=f.readlines()
    f1=open('sample.txt','w')
    for line in lines:
        l=line.split('|')
        if l[0]=='ash':
            flag=True
            continue
        else:
            f1.write(line)
    if flag==False:
        print("not found")

check()
