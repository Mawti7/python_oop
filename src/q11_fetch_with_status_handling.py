# HTTP Exercise: Status Handling with Error Management
# Demonstrates HTTP status handling and exception management

import requests

def fetch_data(url: str) -> None:
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print("Success")
        elif 400 <= response.status_code <= 499:
            print("Client Error")
        elif 500 <= response.status_code <= 599:
            print("Server Error")
        else:
            print(f"Unexpected status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Connection Error: Unable to connect to the server")
    except requests.exceptions.Timeout:
        print("Timeout Error: Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

if __name__ == "__main__":
    # Test URLs
    test_urls = [
        "https://jsonplaceholder.typicode.com/posts/1",  # Should be 200
        "https://jsonplaceholder.typicode.com/invalid",  # Should be 404
        "http://does-not-exist.example"  # Should raise ConnectionError
    ]
    
    for url in test_urls:
        print(f"\nTesting URL: {url}")
        fetch_data(url)
