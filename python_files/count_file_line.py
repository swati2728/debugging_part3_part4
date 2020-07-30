# question2
#( count the line in file )

my_file = open("files.txt","r") 
Counter = 0
file = my_file.read() 
list1 = file.split("\n")   
for i in list1: 
    if i: 
        Counter=Counter+1          
print("This is the number of lines in the file") 
print(Counter) 
