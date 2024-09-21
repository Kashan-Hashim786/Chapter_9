with open("poem.txt","r") as f:
   
   content = f.read()
   if "Twinkle" in content:
      print("Twinkle is present in the content")
   else:
      print("Twinkle is not present in the content")
    