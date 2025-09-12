# HTTP Exercise: PUT & DELETE Requests
# Demonstrates PUT and DELETE HTTP methods

import requests
import json

def do_put():
    # Make PUT request with updated JSON payload
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "id": 1,
        "title": "Updated Post Title",
        "body": "This is an updated post body for the OOP assignment",
        "userId": 1
    }
    
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, json=payload, headers=headers, timeout=5)
    
    print(f"PUT Response Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print("PUT Response JSON:")
        print(json.dumps(response.json(), indent=2))
    
    return response.status_code

def do_delete():
    # Make DELETE request
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url, timeout=5)
    
    print(f"DELETE Response Status Code: {response.status_code}")
    return response.status_code

if __name__ == "__main__":
    print("PUT status:", do_put())
    print("\n" + "="*50 + "\n")
    print("DELETE status:", do_delete())
