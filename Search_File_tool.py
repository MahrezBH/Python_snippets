import fnmatch
import os
rootPath = input("Enter the path to searsh in  ")
pattern = input("Enter the file/dic name with his extension  ")
print("------------------------------------------------------------------------------------")
print("--------------------------------- Researsh Started ----------------------------------")
print("")

for root, dirs, files in os.walk(rootPath):
   for filename in fnmatch.filter(files, pattern):
       print( os.path.join(root, filename))
       
print("")
print("--------------------------------- Researsh Finished ---------------------------------")
print("------------------------------------------------------------------------------------")
