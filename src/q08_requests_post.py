# HTTP Exercise: POST JSON Request
# Demonstrates POST requests with JSON payload

import requests
import json

def main():
    # Make POST request with JSON body
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "OOPs Assignment",
        "body": "Learning Python requests",
        "userId": 101
    }
    
    # Set headers to indicate JSON content
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers, timeout=5)
    
    # Print status code
    print(f"Status Code: {response.status_code}")
    
    # Print response JSON
    if response.status_code in [200, 201]:
        data = response.json()
        print("Response JSON:")
        print(json.dumps(data, indent=2))
        
        # Specifically mention the ID if present
        if "id" in data:
            print(f"\nCreated post with ID: {data['id']}")
    else:
        print(f"Request failed. Response: {response.text}")

if __name__ == "__main__":
    main()
