const int sizes=64;
const int Ports[]={0,2,3,4,5,6,7};
int Re[sizes]={0};
int n;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
for(int i=0;i<10;i++){
delay(300);
Serial.println(i);}

}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()){
   delay(30);
    n=0;
while(Serial.available()){//读取串口缓冲区所有数据
  Re[n]=Serial.read();
  //Serial.println(Re[n]);
  n++;
    }

if((Re[n-1]<=100){
  Serial.println("data wrong!");//最后一位仍然不是100，发送数据错误信息
  for(int i=0;i<sizes;i++){//数据错误清空数据
  Re[i]=0;
  }
    }
}
n=0;
while(Re[n]!=0){//解码部分
  Serial.print("d");
  if(Is1100(Re[n])&&(Re[n+1]>100)){//第一个和第二个数字是0-99，第三位是分隔号100
    int t=(Re[n]-1)*100+Re[n+1]-101;
    Decode(t);}
  else {
    n++;
    if(Is1100(Re[n])&&(Re[n+1]>100)){//第一个和第二个数字是0-99，第三位是分隔号100
    int t=Re[n]*100+Re[n+1];
    Decode(t);}  
  }
n+=2;
  }
for(int i=0;i<sizes;i++){//处理完数据重置数组
  Re[i]=0;
  }
}
bool Is1100(int t){
  if(t>=1&&t<101)return true;
  else return false;
  }
void Decode(int code){
int Port=code&15;
int Value=code>>5;
  Action(Port,Value);
  }
void Action(int Port,int Value){
  if(Value==7)Value=0;//受到发送端无法发送0的限制
  if(Ports[Port]){
    if(Value==255)digitalWrite(Ports[Port],HIGH);//Value为0直接用digital
    else if(!Value)digitalWrite(Ports[Port],LOW);
    else analogWrite(Ports[Port],Value);
    Serial.print("s");
    Serial.print(Ports[Port]);
    Serial.print(":");
    Serial.println(Value);
  }
  }
