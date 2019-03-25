import processing.serial.*;
import java.io.*;

int mySwitch=0;
int counter=0;
int no_lines=0;
String [] subtext1;
String [] subtext = new String[100];

Serial myPort;


void setup(){
 mySwitch=1;
 counter = 0;
 myPort = new Serial(this, "COM14", 9600);
 myPort.bufferUntil('\n');
 myPort.write("asda");
}

void draw() {
 if (mySwitch==1){
   /*The readData function can be found later in the code.
   This is the call to read a CSV file on the computer hard-drive. */
   readData("C:/Users/Pragna/Desktop/out.txt");
   /*The following switch prevents continuous reading of the text file, until
   we are ready to read the file again. */
   mySwitch=0;
 }
 
 /*Only send new data. This IF statement will allow new data to be sent to
 the arduino. */
 
 if(counter<no_lines && mySwitch==0){
   /* Write the next number to the Serial port and send it to the Arduino 
   There will be a delay of half a second before the command is
   sent to turn the LED off : myPort.write('0'); */
   myPort.write(subtext[counter]);System.out.println(subtext[counter] + counter);
   // Sends each line to the serial every 4sec.
   delay(8000);
   System.out.println("---------------------");
   //Increment the counter so that the next number is sent to the arduino.
   counter++;
 }
 else {
   mySwitch=1;
 }
}


/* The following function will read from a CSV or TXT file */
void readData(String myFileName){
 int count_no_lines = 0;
 File file=new File(myFileName);
 BufferedReader br=null;
 BufferedReader br1=null;
 
 try{
   br1=new BufferedReader(new FileReader(file));
   while((br1.readLine())!=null){
     count_no_lines++;
   }
   if(count_no_lines==no_lines){mySwitch=3;}
   else{
     counter=no_lines;
     no_lines=0;
   }
 }
 catch(FileNotFoundException e){
   e.printStackTrace();
 }
 catch(IOException e){
   e.printStackTrace();
 }
 finally{
   try {
     if (br1 != null){
       br1.close();
     }
   }
   catch (IOException e) {
     e.printStackTrace();
   }
 }
 
 try{
   br=new BufferedReader(new FileReader(file));
   String text=null;
   int count=0;
   /* keep reading each line until you get to the end of the file */
   while(mySwitch!=3 && (text=br.readLine())!=null){
     /* Spilt each line up into bits and pieces using a '\n' as a separator */
     subtext1 = splitTokens(text,"\n");
     subtext[count] = subtext1[0];
     count++;
     no_lines++;
   }
   //System.out.println(no_lines);
 }
 catch(FileNotFoundException e){
   e.printStackTrace();
 }
 catch(IOException e){
   e.printStackTrace();
 }
 finally{
   try {
     if (br != null){
       br.close();
     }
   }
   catch (IOException e) {
     e.printStackTrace();
   }
 }
}
