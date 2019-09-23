import os

#get current working directory
print(os.getcwd)

#get Windows log in account name
print(os.getlogin())

#change Working directory. Enter full directory name as argument
os.chdir("C:/Users/Monty/Documents")

#create directory folder. Arugment is folder name
os.mkdir("My New Python Folder")

#delete folder
os.rmdir("My New Python Folder")

#rename file
os.rename(current_file_name, new_file_name)

#delete file
os.remove(file_name)

#additional resources
#https://www.tutorialsteacher.com/python/os-module
