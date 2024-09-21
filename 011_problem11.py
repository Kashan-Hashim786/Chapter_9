import os

def rename_file(oldFile,newFile):
 os.rename(oldFile,newFile)


sourceFile = "oldFile.txt"
destinationFile = "renamed_by_ python.txt"
rename_file(sourceFile,destinationFile)
