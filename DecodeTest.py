def NewEncode(value,index):
    t=(value<<5)+index
    print(t)
    return [int(t/100)+1,(t%100)+101]
def NewDecode(t):
    t=100*(t[0]-1)+t[1]-101
    index=t&31
    value=t>>5
    return [value,index]
while 1:
    value=int(input())
    index=int(input())
    t=NewEncode(value,index)
    print(NewDecode(t))
