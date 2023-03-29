

# Sources: 
# https://www.w3schools.com/python/python_try_except.asp
# https://bobbyhadz.com/blog/python-input-yes-no
# https://www.geeksforgeeks.org/python-requests-tutorial/
# https://realpython.com/python-requests/




import requests

# prompt user for destination URL and HTTP method
url = input("Please enter the destination URL: ")

# Selection is case SENSITIVE....responding with lower case will abort!!
http_method = input("Please select HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# print the request to the screen and ask for confirmation
print(f"Sending {http_method} request to {url}")

# Confirm moving forward
# Any answer other than 'y' will abort
confirmation = input("Do you want to continue?... (y/n): ")
if confirmation.lower() != 'y':
    print("Aborting request...")
    exit()

# Perform the request using requests library
# URL > From USER input*
try:
    if http_method == "GET":
        response = requests.get(url) 
    elif http_method == "POST":
        response = requests.post(url)
    elif http_method == "PUT":
        response = requests.put(url)
    elif http_method == "DELETE":
        response = requests.delete(url)
    elif http_method == "HEAD":
        response = requests.head(url)
    elif http_method == "PATCH":
        response = requests.patch(url)
    elif http_method == "OPTIONS":
        response = requests.options(url)
    else:
        print("Invalid HTTP method...")
        print("Aborting")
        exit()
except requests.exceptions.RequestException as e:
    print(f"An error occurred while performing request: {e}")
    exit()
 

# Print the entire request sent
print(f"\nREQUESTED URL:\n{response.request.url}")
print(f"\nREQUEST TYPE:\n{response.request.method}\n")


# Translate the status code to plain terms, Top 10 Status Codes defined below as example.
status_codes = {
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}


# Print the status code in plain terms
if response.status_code in status_codes:
    print(f"STATUS CODE: \n{response.status_code} - {status_codes[response.status_code]}")
else:
    print(f"STATUS CODE: \n{response.status_code}")
