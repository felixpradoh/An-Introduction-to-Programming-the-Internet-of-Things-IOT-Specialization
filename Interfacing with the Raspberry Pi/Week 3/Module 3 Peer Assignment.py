# Needed package
import http.client

# Choose the url as string
url = "www.uci.edu"

# Stablish the connection to the http website
connection = http.client.HTTPSConnection(url)
connection.request("GET","/")

# Get a response

response = connection.getresponse()

# Read the content
content=response.read(1000)
print(content)

# Close the connection
connection.close()
