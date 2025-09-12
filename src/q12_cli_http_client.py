"""
HTTP Exercise: Mini CLI HTTP Client
Demonstrates command-line HTTP client with multiple methods

Author: Aditya Kasyap
Website: https://www.adityakasyap.com
"""

import sys
import json
import requests

def main(argv):
    if len(argv) < 2:
        print("Usage: python q12_cli_http_client.py <METHOD> <URL> [JSON_BODY]")
        print("Methods: GET, POST, PUT, DELETE")
        print("Example: python q12_cli_http_client.py GET https://jsonplaceholder.typicode.com/posts/1")
        print("Example: python q12_cli_http_client.py POST https://jsonplaceholder.typicode.com/posts '{\"title\":\"x\",\"body\":\"y\",\"userId\":1}'")
        return
    
    method = argv[0].upper()
    url = argv[1]
    json_body = argv[2] if len(argv) > 2 else None
    
    # Validate method
    valid_methods = {"GET", "POST", "PUT", "DELETE"}
    if method not in valid_methods:
        print(f"Error: Invalid method '{method}'. Must be one of: {', '.join(valid_methods)}")
        return
    
    try:
        # Parse JSON body if provided
        data = None
        if json_body:
            try:
                data = json.loads(json_body)
            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON in body - {e}")
                return
        
        # Make the request
        headers = {"Content-Type": "application/json"} if data else {}
        
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        
        # Print results
        print(f"Status Code: {response.status_code}")
        
        # Try to parse response as JSON, fallback to text
        try:
            response_data = response.json()
            print("Response JSON:")
            print(json.dumps(response_data, indent=2))
        except json.JSONDecodeError:
            print("Response Text:")
            print(response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

if __name__ == "__main__":
    main(sys.argv[1:])
