with open("log.txt") as f:
    content = f.read()

if "Python" in content:
    print("Python exists in the content")
else:
    print("Python does not exist in the content")