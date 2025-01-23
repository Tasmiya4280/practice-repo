#list the files in the folders provided provided by the user

import os

folders = input("Enter the folders separated by space to list the files inside : ").split()
for folder in  folders :

  try :
      files = os.listdir(folder)

  except FileNotFoundError:
      print ("provide a valid folder may be that folder does not  exist " + folder)
      continue
  except PermissionError:
      print("you don't have access to this folder " + folder)

  print (".......list of files " +folder)


  for file in files:
      print(file)
