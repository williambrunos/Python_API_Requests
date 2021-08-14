import requests as rq

# Base URL to get the data from the API
base_url = 'http://www.boredapi.com/api/activity/'

# Pay Load to get data with just 1 participant
# The payload accepts more than just one parameter => accepts a dictionary of
# parameters
payload = {'partiipants': 1}

# Doing a request for the API on the base URL to get the params data
request = rq.get(base_url, params=payload)

# Parsing the data from the request to JSON and assigning it for the 'data' variable
data = request.json()

print('----------------------------')
print('The data response')
print('Response: ', data)
print('----------------------------')
print('All the informations in data response')

for information in data:
  print(information)
