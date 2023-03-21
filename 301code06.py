import os

# Run 'whoami' command and store the output in a variable
whoami_output = os.popen('whoami').read()

# Run'ip a' command and store the output in a variable
ip_output = os.popen('ip a').read()

# Run 'lshw -short' command and store the output in a variable
lshw_output = os.popen('lshw -short').read()

# Print the contents of the variables
print("The output of 'whoami' command is:....")
print(whoami_output)

print("The output of 'ip a' command is:....")
print(ip_output)

print("The output of 'lshw -short' command is:....")
print(lshw_output)


