import requests
from auth_token import get_token

def main():
    #Execution begins here.

    token = get_token()

    api_path = "https://sandboxdnac.cisco.com/dna"
    headers = {"Content-Type": "application/json", "X-Auth-Token": 'token'}

    get_resp = requests.get(api_path + '/intent/api/v1/network-device', headers=headers)

    import json; print(json.dumps(get_resp.json(), indent=2))
    #print(device_resp.text.encode('utf8'))

if __name__ == "__main__":
    main() 