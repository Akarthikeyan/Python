To open a txt or any doc using python
  f=open("C:/tmp.txt","r")
  str=f.read()
  print(str)
To print the specified file path and name
  print(f.name)
To check which mode i.e., read or write
  print(f.mode)
To print as false
  print(f.closed)
To print as true
  f.close()
To tell the cursor position
  print(f.tell())
To rename a filename
  import os
  os.rename("d:/kar.txt","d:/thi.txt")
To print the current directory of file
  print(os.getcwd())
To change the directory
  os.chdir("D:/")
To remove the directory
  os.rmdir("D:/")
To remove a file
  os.remove("D:/")
To make a folder on the current directory
  os.mkdir("folder_name")
