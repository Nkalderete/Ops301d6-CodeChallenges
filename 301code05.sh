#!/bin/bash



# Clear Log files

# https://computingforgeeks.com/how-to-empty-truncate-log-files-in-linux/

# COMPRESS CONTENTS TO BACK UP DIRECTORY
#Varibles
MakeLogFile (){
    source_path="/var/log/syslog"
    dest_path=$(pwd)
    source_path2="/var/log/wtmp"
    dest_path2=$(pwd)


    # Set filename to todays date
    filename=$(date +"%Y-%m-%d-%H-%M")
    filename2=$(date +"%Y-%m-%d")


    #copy
    cp "$source_path" "$dest_path/$filename"
    cp "$source_path2" "$dest_path2/$filename2"
}
read -p "would you like to create a file log? 1 for YES, 2 for NO, 3 to EXIT..." Choice


#choice options
case $Choice in
    1)
        echo "File created, continue to next steps..."
        MakeLogFile
        ;;
    2)
        echo "Continue to next..."
        ;;
    3)
        echo "EXITING"
        exit 0
        ;;
esac
clear


while true; do
# Prompt user for logfile
    read -p "Which log would you like to clear?" Logfile


#Var
    Filesize=$(stat -c%s "$Logfile")
    echo "size of $logfile = $Filesize bytes"
    read -p "Are you sure? 1 for Yes, 2 for No, 3 to Exit..." Choice


#choice options
    case $Choice in
        1)
            echo "Log is cleared"
            :> $Logfile
            read -p "Enter to continue"
            ;;
        2)
            echo "Log was not cleared"
            read -p "Enter to continue"
            ;;
        3)
            echo "EXITING"
            exit 0
            ;;
    esac
done
#end