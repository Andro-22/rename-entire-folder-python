import os
os.chdir('C:\\Users\\Andro\\Documents\\Hello')
i=1
for file in os.listdir():
      filesplit = os.path.splitext(file) # filesplit[0] is the file name, filesplit[1] is the extension
      source = file
      dest = "file" + str(i) + filesplit[1] # "file" + a number
      os.rename(source,dest)    #renames the file to "file" + a number
      i+=1