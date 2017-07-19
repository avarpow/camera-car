from PIL import Image
from numpy import *
import time
import math
im=Image.open('12.jpg')
size=im.size

tu=array(im)
stx=20
sty=20
sp=int(min(size[0],size[1])/stx)
x=0
y=0
xx=0
yy=0
n=0
maxxx=0
maxyy=0
maxv=0
v=0
time1=time.time()
while x<size[0]-sp-1:
    while y<size[1]:
        n+=1
        if not n%500:
            per=100*n/size[0]/size[1]*20*20
            c=0
            for i in range(math.ceil(per*20/100)):
                print('■',end='')
                c+=1
            while c<20:
                print('□',end='')
                c+=1
            print('%.2f'%per,'%')
        r=0
        g=0
        b=0
        while x<(xx+stx):
            while y<(yy+sty):
                if x>=xx:
                    if x>=4160 or y>=3120:print('!====')
                    #print(x,y)
                    #print(n)
                    #print(tu[x,y])
                    try:r+=tu[y,x][0]
                    except:print(x,y,n)
                    g+=tu[y,x][1]
                    b+=tu[y,x][2]
                y+=1
            y-=sty
            x+=1
        v=r/(g+b)
        if v>maxv:
            maxxx=xx
            maxyy=yy
            maxv=v
        x-=1
        x-=stx
        y+=sty
        yy+=sty
    y-=sty
    x-=sp
    x+=stx
    yy=0
    xx+=stx
print('用时',time.time()-time1,'秒')
print('区块x像素点位置:',maxxx,'\n区块y像素位置',maxyy,'\n最大相对值',maxv)
