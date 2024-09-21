with open("log.txt") as f:
    lines = f.readlines()
    
lineNo = 1
for line in lines:
   if "Python" in line:
      print(f"Python exists in the line, Line no {lineNo}")
      break
   lineNo += 1
else:
    print("Python does not exist in the line")

        