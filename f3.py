with open('globulete.txt','r') as f:
    a=f.readline()
    al=int(a)
r=al+3
b=(al+r)-2
total=al+r+b
with open ('bradut.txt','w') as f:
    f.write(str(total))