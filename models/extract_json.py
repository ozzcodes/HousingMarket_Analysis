import json
import requests


response = requests.get('https://www.zillow.com/homes/Plymouth-County,-MA_rb/')
todos = json.loads(response.text)

print(todos)

# with open("../data/plymouth_county_zillow.json", "r") as read_file:
#     data = json.load(read_file)
#
# print(data)
