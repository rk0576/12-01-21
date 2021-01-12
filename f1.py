with open ('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    x=int(a)
    y=int(b)
else:
    x=int(b)
    y=int(a)
n=x*2
m=y*3
with open ('produs.txt','w') as f:
    f.write(str(n))
    f.write('      ')
    f.write(str(m))