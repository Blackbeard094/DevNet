import requests
#import json

def get_token():
    
    api_path = "https://sandboxdnac.cisco.com/dna"
    auth = ("devnetuser", "Cisco123!")
    headers = {"Content-Type": "application/json"}

    auth_resp = requests.post(api_path + '/system/api/v1/auth/token', auth=auth, headers=headers)

    auth_resp.raise_for_status()
    token = auth_resp.json() ["Token"]
    print(token)
    #print("Token: {}".format(token))

    return token

def main():

    token = get_token()

    api_path = "https://sandboxdnac.cisco.com/dna"
    headers = {"Content-Type": "application/json", "X-Auth-Token": token}

    get_device = requests.get(api_path + '/intent/api/v1/network-device', headers=headers)
    #print(get_device.request.method)
    #print(get_device.request.headers)
    #print(get_device.request.body)

    import json; 
    print(json.dumps(get_device.json(), indent=2))
    #print(get_device.text.encode('utf8'))

if __name__ == "__main__":
    main() 