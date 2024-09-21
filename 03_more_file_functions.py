f = open("file1.txt")



lines = f.readlines()
print(lines,type(lines)) # read all lines in form of list

line1 = f.readline()  # read one line at a time in form of string
print(line1,type(line1))

line2 = f.readline()  # read one line at a time in form of string
print(line2,type(line2))

line3 = f.readline()  # read one line at a time in form of string
print(line3,type(line3))

line4 = f.readline()  # read one line at a time in form of string
print(line4,type(line4))

line5 = f.readline()  # read one line at a time in form of string
print(line5 == "")

line6 = f.readline()  # read one line at a time in form of string
print(line6)

f.close()


