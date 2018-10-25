

myList =[1,2,3,4]

my_file = open("firstfile.txt","w")
for item in myList:
    my_file.write(str(item)+"\n")

my_file.close()