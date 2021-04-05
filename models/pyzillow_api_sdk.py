import requests

url = "https://www.zillow.com/homes/Plymouth-County,-MA_rb/"

payload = "zpid=%3CREQUIRED%3E&chartDuration=%5B%221year%22%2C%225years%22%2C%2210years%22%5D&unit-type=dollar&zws-id" \
          "=%3CREQUIRED%3E "
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "0b6e659976msh33d9dcf51fc07dcp161394jsn637923d981f1",
    'x-rapidapi-host': "ZillowdimashirokovV1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
