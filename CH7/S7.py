# You can give different value to different parameter.
def myfnc(x,z,y=10):
    print('x =',x,'y =',y,'z =',z)

myfnc(x=1,y=2,z=3)
a=5
b=6
myfnc(x=a,z=b)
a=1
b=2
c=3
myfnc(y=a,x=b,z=c)