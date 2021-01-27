import requests

def get_token():
    #Get an access token from the Cisco DNAC. Return the token string if successful; Faulse otherwise.
    
    api_path = "https://sandboxdnac.cisco.com/dna"
    auth = ("devnetuser", "Cisco123!")
    headers = {"Content-Type": "application/json"}

    #Issue HTTP POST request to the proper URL to request a token
    auth_resp = requests.post(api_path + '/system/api/v1/auth/token', auth=auth, headers=headers)

    #If successful, Print token. Else, raise HTTPError with details
    auth_resp.raise_for_status()
    token = auth_resp.json() ["Token"]
    print(token)

def main():
    #Execution begins here.

    token = get_token()
    #print(token)

    api_path = "https://sandboxdnac.cisco.com/dna"
    X-Auth-Token = {"token"}
    headers = {"Content-Type": "application/json"}

    auth_resp = requests.get(api_path + '/intent/api/v1/network-device', X-Auth-Token=X-Auth-Token, headers=headers)

    auth_resp.raise_for_status()

if __name__ == "__main__":
    main()