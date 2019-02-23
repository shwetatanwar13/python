file=open("test1.txt","w")
file.write("MArk")
file.seek(1)
file.write("Smart")
file.write("you")
file.seek(4)
file.write("stupid")
file.close()

file=open("test1.txt","a+")
file.write("MArk")
file.close()

file=open("test1.txt","w")
file.write("12")
file.close()


