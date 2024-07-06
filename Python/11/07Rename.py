import os
# Defining the Old and new File Name
oldname="old.txt"
newname="Newly_Rename_File.txt"

# Reading the Content of Old FIles
with open(oldname) as f:
    data=f.read()

# Writing the COntent in New FIles
with open(newname,"w") as f:
    f.write(data)

# Os Module to Rename the File Names
# os.rename(newname,oldname)

# Removing the Old Files
os.remove(oldname)