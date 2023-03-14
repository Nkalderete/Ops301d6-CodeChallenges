#!/bin/bash


# filename variable
filename="syslog_$(date +%Y-%m-%d_%H-%M)"


# copies /var/log/syslog to file 
cp /var/log/syslog "$filename"



echo "Copied /var/log/syslog to $filename"
