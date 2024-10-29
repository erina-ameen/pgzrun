#Opening File
file=open("file1.txt","r")
for i in file:
    print(i)

#Method 2
file=open("file1.txt","r")
#print(file.read())
print(file.read(3))

#Writing a File
file=open("file1.txt","w")
file.write("what is your name?\n")
file.write("where are you from?\n")
file.close()

#Append File
file=open("file1.txt","a")
file.write("my name is erina")
file.close()
