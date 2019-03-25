##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
import serial
import sys
print(sys.argv[1])

serial_port = 'COM10';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
write_to_file_path1 = ("C:\\Users\\saiteja\\Desktop\\output1.txt");
output_file1 = open(write_to_file_path1, "w");

write_to_file_path2 = ("C:\\Users\\saiteja\\Desktop\\output2.txt");
output_file2 = open(write_to_file_path2, "w");
ser = serial.Serial(serial_port, baud_rate)
temp = []
while True:
    line = ser.readline();
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    s=line.split("/");
    if not line.strip():
        continue
    print(line);
    if(int(sys.argv[1]) == 3 and len(temp) == 2):
        break
    if(int(sys.argv[1]) == 1 or int(sys.argv[1]) == 3):
        if(s[0]=='1' and '!!~~' not in s[1]):
            output_file1.write(s[1]);
        if(s[0]=='1' and '!!~~' in s[1]):
            temp.append(line)
        if(int(sys.argv[1]) == 1 and len(temp) == 1):
            break
    if(int(sys.argv[1]) == 2 or int(sys.argv[1]) == 3):
        if(s[0]=='2' and '!!~~' not in s[1]):
            output_file2.write(s[1]);
        if(s[0]=='2' and '!!~~' in s[1]):
            temp.append(line)
        if(int(sys.argv[1]) == 2 and len(temp) == 1):
            break 
