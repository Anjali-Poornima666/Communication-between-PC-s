import os
folder = '/home/chadalavada/Desktop/Fcomm_ANJALI/video_to_image'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)


os.system('ffmpeg -i /home/chadalavada/Desktop/Fcomm_ANJALI/input_videos/test_video2.mp4 -vf fps=1/2 /home/chadalavada/Desktop/Fcomm_ANJALI/video_to_image/test%1d.jpg')


DIR = '/home/chadalavada/Desktop/Fcomm_ANJALI/video_to_image'
no_of_img = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

out_file = open('/home/chadalavada/Desktop/Fcomm_ANJALI/output.txt', 'w')
out_file.write('')
out_file.close

out_file = open('/home/chadalavada/Desktop/Fcomm_ANJALI/output.txt', 'a')

for i in range(1, no_of_img+1):
	#os.system('tesseract /home/anjali/Desktop/Fcomm_ANJALI/input_images/test' + str(i) + '.jpg out -l eng+hin+deu')
	os.system('tesseract /home/chadalavada/Desktop/Fcomm_ANJALI/video_to_image/test' + str(i) + '.jpg out -l eng')
	
	fp = open('out.txt', 'r')
	for line in fp:
		if not line.strip():
			continue
		elif i == no_of_img:
			out_file.write(line)
	fp.close()
	#out_file.write('-----------------'  + '\n')
out_file.close
