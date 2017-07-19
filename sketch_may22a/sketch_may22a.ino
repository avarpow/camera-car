const int left1=2;//2-7引脚分别控制左右马达
const int leftPWM=3;
const int left2=4;
const int right1=5;
const int rightPWM=6;
const int right2=7;
const int sizes=64;
int Servo1last;
int Servo2last;
int Servo3last;
unsigned long lasttime;
int Re[sizes]={0};
int n;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
for(int i=0;i<10;i++){//
delay(300);
Serial.println(i);}
lasttime=millis();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(millis()-lasttime>2000){//每两秒读取传感器
    //do
    lasttime=millis();
    }
  if(Serial.available()){
     delay(30);
     n=0;
     while(Serial.available()){//读取串口缓冲区所有数据
       Re[n]=Serial.read();
       //Serial.println(Re[n]);
       n++;
         }

  if((Re[n-1]<=100)){
    Serial.println("data wrong!");//最后一位<100，发送数据错误信息
    for(int i=0;i<sizes;i++){//数据错误清空数据
    Re[i]=0;
    }
      }
  }
  n=0;
  while(Re[n]){//解码部分
    Serial.print("d");
      if(Is1100(Re[n])&&(Re[n+1]>100)){//第一个<100,第二个大于100
        int t=(Re[n]-1)*100+Re[n+1]-101;//复原原始十进制数
        Decode(t);}
      else {
        n++;
        if(Is1100(Re[n])&&(Re[n+1]>100)){//默认为数据出现了位移，从后一位开始解码
          int t=Re[n]*100+Re[n+1]-101;
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
int Port=code&31;
int Value=code>>5;
  Action(Port,Value);
  }

  
void Action(int Port,int Value){
  //if(Value==7)Value=0;//受到发送端无法发送0的限制
   if(!(Port>>2)){//控制左马达
    digitalWrite(left1,Port&1);
    digitalWrite(left2,(Port>>1)&1);
    analogWrite(leftPWM,Value);
    }
   else if((Port>>2)==1){
    digitalWrite(right1,Port&1);
    digitalWrite(right2,(Port>>1)&1);
    analogWrite(rightPWM,Value);
    }
   else if((Port>>2)==2){//1000-1011
    if(!(Port&3)){
      
      }
    if(Port&3==1){
          
      }
    if(Port&3==2){
      
      }
    if(Port&3==3){
      
      }
    }
   else if((Port>>2)==3){//1100-1111组网控制预留
    if(!(Port&3)){
      
      }
    if(Port&3==1){
          
      }
    if(Port&3==2){
      
      }
    if(Port&3==3){
      
      }
    }

  }
