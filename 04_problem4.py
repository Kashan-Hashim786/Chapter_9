def replaceText():
    with open("04_problem4.txt","r") as f:
     content = f.read()
     contentNew = content.replace("donkey","#####")
     with open("04_problem4.txt","w") as f:
        f.write(contentNew)

replaceText()