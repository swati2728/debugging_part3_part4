new_file=open("file_question4.txt",'r')
# print(new_file.read())
for line in (new_file):
	# print(i)
	if "delhi" in line:
		print(line)
		delhi=open("delhi.txt",'a')
		delhi.write(line)
	elif "shimla" in line:
		print(line)
		shimla=open("shimla.txt",'a')
		shimla.write(line)		
new_file.close()

	