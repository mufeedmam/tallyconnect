import requests
import json
import sys

def check_connection():
    print("ERPNext Connectivity Diagnoser")
    print("------------------------------")
    
    if len(sys.argv) == 4:
        url = sys.argv[1]
        api_key = sys.argv[2]
        api_secret = sys.argv[3]
        print(f"Using credentials from command line for: {url}")
    else:
        try:
            url = input("Enter ERPNext URL (e.g., https://yourserver.com): ").strip()
            if not url:
                print("URL is required.")
                return

            api_key = input("Enter API Key: ").strip()
            if not api_key:
                print("API Key is required.")
                return

            api_secret = input("Enter API Secret: ").strip()
        except EOFError:
            print("Error: Input stream closed. Please provide arguments: python check_connection.py <URL> <API_KEY> <API_SECRET>")
            return
            
        if not api_secret:
            print("API Secret is required.")
            return

    # Removing trailing slash if present
    if url.endswith('/'):
        url = url[:-1]

    # Construct headers
    headers = {
        'Authorization': f'token {api_key}:{api_secret}',
        'Accept': 'application/json'
    }

    # 1. Test basic connectivity and auth using get_logged_user
    print(f"\nTesting connection to {url}...")
    test_endpoint = f"{url}/api/method/frappe.auth.get_logged_user"
    
    try:
        try:
            response = requests.get(test_endpoint, headers=headers, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"\n[ERROR] Connection failed: {e}")
            print("Please check:\n1. The URL is correct.\n2. You are connected to the internet.\n3. The server is reachable.")
            return

        if response.status_code == 200:
            print("\n[SUCCESS] Connection Established!")
            print(f"Logged in User: {response.json().get('message')}")
        elif response.status_code == 401 or response.status_code == 403:
            print(f"\n[ERROR] Authentication failed (Status {response.status_code}).")
            print("Please check your API Key and API Secret.")
        elif response.status_code == 404:
            print(f"\n[ERROR] Endpoint not found (Status 404).")
            print(f"Tried accessing: {test_endpoint}")
            print("Please check if the URL is pointing to a valid ERPNext instance.")
        else:
            print(f"\n[ERROR] Unexpected response: {response.status_code}")
            print(response.text)

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_connection()
