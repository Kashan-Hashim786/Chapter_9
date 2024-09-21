def replaceText():
    words = ["Karachi","Multan","Islamabad"]
    with open("04_problem4.txt","r") as f:
        content = f.read()

    for word in words:
        content = content.replace(word,"#####")

    with open("04_problem4.txt","w") as f:
        f.write(content)

replaceText()