import http.client
import random
import json

connection = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
payload = ''
headers = {}
connection.request("GET", "/api/stockexchanges", payload, headers)
response = connection.getresponse()
data = response.read()
print(data.decode("utf-8"))



conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
payload = ''
headers = {}
conn.request("GET", "/api/shareslist/Warszawa", payload, headers)
res = conn.getresponse()
data2 = res.read()
print(data2.decode("utf-8"))


conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
payload = ''
headers = {
  'Authorization': 'Basic MDExNTg2NTZAcHcuZWR1LnBsOjgrdWYrNWQ=',
  'Cookie': 'ARRAffinity=17d4a7379fd5208547170b80243178455a569b5053598ccf1b21a534dff90a54; ARRAffinitySameSite=17d4a7379fd5208547170b80243178455a569b5053598ccf1b21a534dff90a54'
}
conn.request("GET", "/api/shareprice/Warszawa?share=ENERGA", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

def buy():
    conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
    payload = json.dumps({
        "stockExchange": "Warszawa",
        "share": "ASSECOPOL",
        "amount": 1,
        "price": 91
    })
    headers = {
        'Authorization': 'Basic MDExNTg2NTZAcHcuZWR1LnBsOjgrdWYrNWQ=',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/buyoffer", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def buy50():

    for i in range(50):
        conn = http.client.HTTPSConnection("zsutstockserver.azurewebsites.net")
        payload = json.dumps({
            "stockExchange": "Warszawa",
            "share": "ASSECOPOL",
            "amount": 1,
            "price": 91
        })
        headers = {
            'Authorization': 'Basic MDExNTg2NTZAcHcuZWR1LnBsOjgrdWYrNWQ=',
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/api/buyoffer", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

buy50()