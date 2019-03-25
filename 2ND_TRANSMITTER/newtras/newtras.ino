#include <VirtualWire.h>
char *controller;
String das;
int alter= 0;

int rec_1 = 2100;
int rec_2 = 2200;

char* string2char(String command){
    if(command.length()!=0){
        char *p = const_cast<char*>(command.c_str());
        return p;
    }
}

void send_data()
{
      
    vw_send((uint8_t *)string2char(das), strlen(string2char(das)));
    vw_wait_tx(); // Wait until the whole message is gone
    vw_setup(5500);
}

void get_req()
{
      das[0] = '2';
      /*for(int i1=0;i1<das.length()-2;i1++)
      {
        das[i1] = das[i1+2];
      }
      das[das.length()-2] = ' ';das[das.length()-1] = ' ';*/
}

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  vw_set_ptt_inverted(true); //
  vw_set_tx_pin(12);
  //vw_setup(4600);// speed of data transfer Kbps
}

void loop(){
  if(Serial.available()){
    das=Serial.readString(); // Reading input as a string.
    delay(500);
    if(das[0] == '1')
    {
      get_req();
      vw_setup(rec_1);
      send_data();
      delay(4000);
    }
    else if(das[0] == '2')
    {
      get_req();
      vw_setup(rec_2);
      send_data();
      delay(4000);
    }
    else if(das[0] == '3')
    {
      get_req();
      vw_setup(rec_1);
      send_data();
      delay(4000);
      vw_setup(rec_2);
      send_data();
    }
    alter = 1-alter;
    digitalWrite(13,alter);
    Serial.println("send again now!!!");
  }
}

