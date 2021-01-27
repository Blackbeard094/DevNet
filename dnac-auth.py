#### DNAC Authentication API ###

import requests

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload = None

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
    "Accept": "application/json"
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

#import http.client
#conn = http.client.HTTPSConnection("sandboxdnac.cisco.com")
#payload = ''
#headers = {
#'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
#}
#conn.request("POST", "/dna/system/api/v1/auth/token", payload, headers)
#res = conn.getresponse()
#data = res.read()
#print(data.decode("utf-8"))