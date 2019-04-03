# Communication-between-PC-s
<ul>
⦁	Initially, we extracted text from videos. i.e., firstly we divided the video into frames and from each frame text is extracted using TESSERACT. </ul>
<ul>⦁	Next, we have done single receiver and single transmitter. We sent a text file from one PC to other using RF transmitter and RF receiver.
</ul>
<ul>⦁	For this, we also have done applet using eclipse. Transmission and Receiving is done using Arduino codes and for this we have written python codes for reading and writing into text files from serial monitor of the Arduino in order to share the text files among the PC’S.</ul>
<ul> ⦁	Next, we tried two receivers. This is achieved by setting the baud rate for different receivers differently (giving unique transmission rates).</ul>
<ul>⦁	For the second receiver, we used processing3 to write into text file from Arduino.
 </ul>
 <ul>⦁	Finally, we achieved MIMO i.e., two transmitters and two receivers. The receiver can select from which transmitter it can receive and transmitter can select to which receiver it should send. All this is controlled from eclipse GUI. </ul>
 
 <h2> How to run </h2>
 The codes for each application are given in the respective folders for transmiter 1 and 2 and also receivers 1 and 2 .
 
