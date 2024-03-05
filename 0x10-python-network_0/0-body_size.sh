#!bin/bash
#Getting URL from the command line argument
url=$1

#Sending request and store response in the variable
response=$(curl -s -w "%{size_download}" -o /dev/null $url)

#Displaying size of the response body
echo "The size of response body is $response bytes"
