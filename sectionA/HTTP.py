from urllib import request

# send a request to open up a url link and save the response in a variable
resp = request.urlopen("https://www.wikipedia.org")

# check the status of the request made
status = resp.code

# save the content in the response in a variable
data = resp.read()

# decode the content according to the type of which it was encoded in
html = data.decode("utf-8")
