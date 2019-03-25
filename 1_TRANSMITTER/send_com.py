import serial,time

serial_port = "/dev/ttyACM0"
baud_rate = 9600
read_from_file = "/home/chadalavada/Desktop/out.txt"
read_file = open(read_from_file, "r")

ser = serial.Serial(serial_port,baud_rate)
for line in read_file:
   print line
   ser.write(line) 
   time.sleep(8)  
