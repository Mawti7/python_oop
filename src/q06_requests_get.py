# HTTP Exercise: Basic GET Request
# Demonstrates basic HTTP GET request and JSON response handling

import requests

def main():
    try:
        # Make GET request to the API
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(url, timeout=5)
        
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
    except requests.exceptions.Timeout:
        print("Request timed out after 5 seconds")
    except requests.exceptions.ConnectionError:
        print("Connection error - unable to reach the server")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
