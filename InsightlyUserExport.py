import requests
import csv
import base64

api_key = 'Your API Key'
url = "https://api.insightly.com/v3.1/Users"

encoded_api_key = base64.b64encode(api_key.encode()).decode()  # encode the API key in base64

headers = {
    "Authorization": f"Basic {encoded_api_key}",
    "Content-Type": "application/json",
}

response = requests.request("GET", url, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    users = response.json()

    # get the keys from the first dictionary in the list, to use as CSV column headers
    fieldnames = users[0].keys()

    with open('InsightlyUsers.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user in users:
            writer.writerow(user)
else:
    print(f"Error: received status code {response.status_code} from the API.")
    print(response.text)
