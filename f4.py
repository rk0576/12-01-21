with open ('input.txt','r') as f:
    a=f.readline()
    x=int(a)
with open ('output.txt','w') as f:
    f.write(str(x-2))
    f.write('  ')
    f.write(str( x-1))
    f.write('  ')
    f.write(str( x))
    f.write('  ')
    f.write(str(x+1))
    f.write('  ')
    f.write(str(x+2))