import fnmatch
import os
rootPath = input("Enter the path to searsh in  ")
pattern = input("Enter the file name with his extension  ")
print("------------------------------------------------------------------------------------")
print("--------------------------------- Researsh Started ----------------------------------")
print("")

exist = False
for root, dirs, files in os.walk(rootPath):
   for filename in fnmatch.filter(files, pattern):
       print( os.path.join(root, filename))
       exist = True
if (not(exist)):
    print(" NO FILE '{}' ".format(pattern))
      
print("")
print("--------------------------------- Researsh Finished ---------------------------------")
print("------------------------------------------------------------------------------------")
