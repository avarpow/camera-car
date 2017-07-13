from tkinter import *
from tkinter import ttk
import serial,time
import serial.tools.list_ports  
port_list = list(serial.tools.list_ports.comports())
if len(port_list):
    for i in port_list:
        print(i[0])
        print(i[1])
    
ser=serial.Serial('COM7')
ser.timeout=0.01

n=0
root=Tk()
root.title('2017课题')
root.geometry('800x640+0+0')#窗口初始化


#==============部件作用函数=============================
def sent(Port,Value):
    if Value<7:Value=7#避免temp不超过100串口数据无法发送
    temp=[]
    c=(Value<<4)+Port
    d=c%100
    c=int(c/100)
    temp.append(c)
    temp.append(d)
    temp.append(100)
    ser.write(temp)
    print(temp)


def Up():
    print('Up')
def Down():
    print('Down')
def Left():
    print('Left')
def Right():
    print('Right')
def Stop():
    print('Stop')
    BoxRec.insert(END,'Stop')
def _Up(event):
    Up()
def _Down(event):
    Down()
def _Left(event):
    Left()
def _Right(event):
    Right()
def _Stop(event):
    Stop()

def Fun1():
    print('Fun1')
    sent(3,127)
def Fun2():
    print('Fun2')
    sent(3,128)
def Fun3():
    print('Fun3')
def Fun4():
    print('Fun4')
    
def YunUp():
    print('YunUp')
def YunDown():
    print('YunDown')
def YunLeft():
    print('YunLeft')
def YunRight():
    print('YunRight')
def YunStop():
    print('YunStop')

def _YunUp():
    YunUp()
def _YunDown():
    YunDown()
def _YunLeft():
    YunLeft()
def _YunRight():
    YunRight()
def _YunStop():
    YunStop()

    
def YunFun1():
    print('YunFun1')
def YunFun2():
    print('YunFun2')
def YunFun3():
    print('YunFun3')
def YunFun4():
    print('YunFun4')


def Send():
    print('send')
def Seclect():
    print('Seclect')
def Baud():
    print('Baud')
    global n
    n=n+1
    Bau.set(n)
def Clear():
    print(clear.get())
def ConStart():
    print('ConStart')
    root.after(1,_ConStart,root)
def _ConStart(widget):
    while ser.in_waiting and (not(ser.out_waiting)):
        t=ser.readline().decode().strip()
        print(t)
        a=time.strftime('[%H:%M:%S]',time.localtime(time.time()))
        BoxRec.insert(END,a+t)
    root.after(10,_ConStart,root)
    
    




#============组件放置=======================

Fm1=Frame(root)

#***********1.操控部件***********
FmBut=LabelFrame(Fm1,text='操控')
Butheight=2
Butwidth=5
ButUp=Button(FmBut,text='↑',command=Up,height=Butheight,width=Butwidth)
ButDown=Button(FmBut,text='↓',command=Down,height=Butheight,width=Butwidth)
ButLeft=Button(FmBut,text='←',command=Left,height=Butheight,width=Butwidth)
ButRight=Button(FmBut,text='→',command=Right,height=Butheight,width=Butwidth)
ButStop=Button(FmBut,text='X',command=Stop,height=Butheight,width=Butwidth)
ButFun1=Button(FmBut,text='功能1',command=Fun1,height=Butheight,width=Butwidth)
ButFun2=Button(FmBut,text='功能2',command=Fun2,height=Butheight,width=Butwidth)
ButFun3=Button(FmBut,text='功能3',command=Fun3,height=Butheight,width=Butwidth)
ButFun4=Button(FmBut,text='功能4',command=Fun4,height=Butheight,width=Butwidth)

ButFun1.grid(row=0,column=0)
ButFun2.grid(row=0,column=2)
ButFun3.grid(row=2,column=0)
ButFun4.grid(row=2,column=2)

ButUp.grid(row=0,column=1)
ButDown.grid(row=2,column=1)
ButLeft.grid(row=1,column=0)
ButRight.grid(row=1,column=2)
ButStop.grid(row=1,column=1)

#**********2.云台操控*****************
FmYun=LabelFrame(Fm1,text='云台操控')

Butheight=2
Butwidth=5
ButYunUp=Button(FmYun,text='↑',command=YunUp,height=Butheight,width=Butwidth)
ButYunDown=Button(FmYun,text='↓',command=YunDown,height=Butheight,width=Butwidth)
ButYunLeft=Button(FmYun,text='←',command=YunLeft,height=Butheight,width=Butwidth)
ButYunRight=Button(FmYun,text='→',command=YunRight,height=Butheight,width=Butwidth)
ButYunStop=Button(FmYun,text='X',command=YunStop,height=Butheight,width=Butwidth)
root.bind('<a>',Up)
ButYunFun1=Button(FmYun,text='动作1',command=YunFun1,height=Butheight,width=Butwidth)
ButYunFun2=Button(FmYun,text='动作2',command=YunFun2,height=Butheight,width=Butwidth)
ButYunFun3=Button(FmYun,text='动作3',command=YunFun3,height=Butheight,width=Butwidth)
ButYunFun4=Button(FmYun,text='动作4',command=YunFun4,height=Butheight,width=Butwidth)

ButYunFun1.grid(row=0,column=0)
ButYunFun2.grid(row=0,column=2)
ButYunFun3.grid(row=2,column=0)
ButYunFun4.grid(row=2,column=2)
ButYunUp.grid(row=0,column=1)
ButYunDown.grid(row=2,column=1)
ButYunLeft.grid(row=1,column=0)
ButYunRight.grid(row=1,column=2)
ButYunStop.grid(row=1,column=1)


#**********3.传感器接受信息************
FmData=LabelFrame(Fm1,text='传感器数据')

#温度
Label(FmData,text='温度').grid(row=0,column=0,sticky=E)

Tpt=StringVar()
Tpt.set(10.343)
LabelTpt=Label(FmData,textvariable=Tpt)
LabelTpt.grid(row=0,column=1,sticky=E)

Label(FmData,text='℃').grid(row=0,column=2,sticky=W)


#湿度
Label(FmData,text='湿度').grid(row=1,column=0,sticky=E)

Wet=StringVar()
Wet.set(45678)
LabelTpt=Label(FmData,textvariable=Wet)
LabelTpt.grid(row=1,column=1,sticky=E)

Label(FmData,text='％').grid(row=1,column=2,sticky=W)

#经度
Label(FmData,text='经度').grid(row=2,column=0,sticky=E)

Lng=StringVar()
Lng.set(132.324134)
LabelLng=Label(FmData,textvariable=Lng)
LabelLng.grid(row=2,column=1,sticky=E)

Label(FmData,text='°E').grid(row=2,column=2,sticky=W)


#纬度
Label(FmData,text='纬度').grid(row=3,column=0,sticky=E)

Lat=StringVar()
Lat.set(132.324134)
LabelLat=Label(FmData,textvariable=Lat)
LabelLat.grid(row=3,column=1,sticky=E)

Label(FmData,text='°N').grid(row=3,column=2,sticky=W)

#可燃气体浓度
Label(FmData,text='可燃气体').grid(row=4,column=0,sticky=E)

Gas=StringVar()
Gas.set(2384)
LabelGas=Label(FmData,textvariable=Gas)
LabelGas.grid(row=4,column=1,sticky=E)

Label(FmData,text='ppm').grid(row=4,column=2,sticky=W)



Label(FmData,text='速度').grid(row=5,column=0,sticky=E)

CarSpeed=StringVar()
CarSpeed.set(243)
LabelCarSpeed=Label(FmData,textvariable=CarSpeed)
LabelCarSpeed.grid(row=5,column=1,sticky=E)

Label(FmData,text='单位待定').grid(row=5,column=2,sticky=W)




#********串口设置*********
FmOpt=LabelFrame(Fm1)
Label00=Label(FmOpt,text='串口号')
Label00.grid(row=0,column=0)


Sec=StringVar()
EntrySec=Entry(FmOpt,textvariable=Sec)
EntrySec.grid(row=0,column=1)

BtnSec=Button(FmOpt,text='连接',command=Seclect,height=1)
BtnSec.grid(row=0,column=2)

Label01=Label(FmOpt,text='波特率')
Label01.grid(row=1,column=0)


Bau=StringVar()
EntryBau=Entry(FmOpt,textvariable=Bau)
EntryBau.grid(row=1,column=1)

BtnBau=Button(FmOpt,text='设置',command=Baud,height=1)
BtnBau.grid(row=1,column=2)





#*************串口收发区**********88
FmSer=Frame(root)


scrollbar = Scrollbar(FmSer)
BoxRec=Listbox(FmSer, yscrollcommand=scrollbar.set,height=20,width=48)
BoxRec.grid(row=0,column=0,rowspan=2,sticky=W)

scrollbar.config(command=BoxRec.yview,width=1)
scrollbar.grid(row=0,column=1,rowspan=2,sticky=N+S+W)

BtuStart=Button(FmSer,text='同步开始',command=ConStart,height=7,width=10)
BtuStart.grid(row=1,column=2)

Rec=StringVar()
Rec.set(45678)

TextRec=Text(FmSer,height=10,width=50)
TextRec.grid(row=2,column=0)

BtuSend=Button(FmSer,text='发送',command=Send,height=7,width=10)
BtuSend.grid(row=2,column=1)

clear=StringVar()
Clear=Checkbutton(FmSer,text='发送后清空',command=Clear,variable=clear)
Clear.grid(row=2,column=2)

#=================按键绑定=================================
root.bind('<Up>',_Up)
root.bind('<Down>',_Down)
root.bind('<Left>',_Left)
root.bind('<Right>',_Right)
root.bind('<space>',_Stop)


#==============布局显示====================================


FmOpt.grid(row=0,column=0)
FmBut.grid(row=2,column=0)
FmYun.grid(row=3,column=0)
FmData.grid(row=1,column=0)
Fm1.grid(row=0,column=0)
FmSer.grid(row=0,column=1,rowspan=2)

root.mainloop()



    
