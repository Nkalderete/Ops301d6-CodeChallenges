#!/bin/bash



# Prompt user for doc
read -p "Directory path you would like to edit permissions?" Directory

# Prompt user for command 
read -p "Type command to change permissions?" Code

# Check file permissions
ls -l "$Directory" 

# Change permissions
chmod -R "$Code" "$Directory"

echo "Permissions for directory and its contents updated successfully" 
