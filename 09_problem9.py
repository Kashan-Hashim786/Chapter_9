with open("this.txt") as f:
    content1 = f.read()

with open("this1.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Both files have same content")
else:
    print("Both files do not have same content")
    