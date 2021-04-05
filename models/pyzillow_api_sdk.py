import requests
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

url = "https://www.zillow.com/homes/Plymouth-County,-MA_rb/"

zillow_data = ZillowWrapper('X1-ZWz16pqqcqqhhn_11xce')
deep_search = zillow_data.get_data("https://www.zillow.com/homes/Plymouth-County,-MA_rb/", {
    'zipcode': '02339'
})



