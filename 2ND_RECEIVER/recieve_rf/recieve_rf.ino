#include <VirtualWire.h>
#include <LiquidCrystal.h>

const int rs = 10, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
int k=0;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int alter = 0;
int i;
String s;



void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 1);
  vw_set_ptt_inverted(true); // Required for DR3100
  vw_set_rx_pin(9);
  vw_setup(2200); // Bits per sec
  pinMode(13, OUTPUT);
  
  vw_rx_start(); // Start the receiver PLL running
}
void loop()
{
  uint8_t buf[VW_MAX_MESSAGE_LEN];
  uint8_t buflen = VW_MAX_MESSAGE_LEN;
  
  if (vw_get_message(buf, &buflen)) // Non-blocking
  {
    s="";
    for(i = 0;i < buflen;i++){
      Serial.print((char)buf[i]);
      s+=(char)buf[i];
      buf[i] = (uint8_t )(' ');
    }

    lcd.print(s);
    delay(150);
    k=s.length();
    for (int positionCounter = 0; positionCounter < k; positionCounter++) {
      // scroll one position left:
      lcd.scrollDisplayLeft();
      // wait a bit:
      delay(250);
    }
    lcd.clear();
    Serial.println();
    alter = 1-alter;
    digitalWrite(13, alter);
  }
}

