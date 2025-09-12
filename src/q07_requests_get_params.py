# HTTP Exercise: GET with Parameters
# Demonstrates GET requests with query parameters and JSON formatting

import requests
import json

def main():
    # Make GET request with parameters
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": 1}
    
    response = requests.get(url, params=params, timeout=5)
    
    # Check if request was successful
    if response.status_code == 200:
        # Get JSON data
        data = response.json()
        
        # Print the length of results
        print(f"Number of comments for postId=1: {len(data)}")
        
        # Print first 2 items (pretty formatted JSON)
        print("\nFirst 2 comments:")
        print(json.dumps(data[:2], indent=2))
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    main()
