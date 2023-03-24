# Import os module to delete file
import os


# 'with open('...', 'w')' = creates file, opens file, writes in file, closes file.
with open('TEST.txt', 'w') as f:


    # Append three lines to file
    #  f.write() used to write data to a file.
    # '\n' = end of the line/ next write-out is for next line
    f.write('This is the first line.\n')
    f.write('This is the second line.\n')
    f.write('This is the third line.\n')


# Open TEST.txt file for reading
# 'r'= read mode
with open('TEST.txt', 'r') as f:


    # Read first line from file
    first_line = f.readline()


    # Print first line to screen
    print(first_line)


# Delete TEST.txt file
os.remove('TEST.txt')




## SOURCES ##

# https://www.geeksforgeeks.org/python-append-to-a-file/
# https://stackoverflow.com/questions/4706499/how-do-i-append-to-a-file
# https://quickref.me/python
# ChatGPT> better understanding of how some of the syntax worked