# HTTP Exercise: Basic GET Request
# Demonstrates basic HTTP GET request and JSON response handling

import requests

def main():
    # Make GET request to the API
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Get JSON data
        data = response.json()
        
        # Print the entire response JSON
        print("Full response JSON:")
        print(data)
        
        # Print specifically the "title" field
        print(f"\nTitle: {data['title']}")
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    main()
