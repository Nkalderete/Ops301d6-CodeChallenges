#!/bin/bash

while true; do
    clear
    echo "Please select an option:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    read -p "Enter your choice: " choice

    case $choice in
        1)
            echo "Hello world!"
            read -p "Press enter to continue"
            ;;
        2)
            ping -c 4 127.0.0.1
            read -p "Press enter to continue"
            ;;
        3)
            ip a 
            read -p "Press enter to continue"
            ;;
        4)
            exit 0
            ;;
        *)
            echo "Invalid choice. Press enter to try again."
            read
            ;;
    esac
done
