import requests

# The target website or IP you want to brute‑force directories on
target_url = "http://10.10.79.13"

# Path to your wordlist containing possible directory names
wordlist_path = 'common.txt'

print(f"[+] Starting directory brute force on: {target_url}!")

# Open the wordlist file and read it line by line
with open(wordlist_path, 'r') as file:
    for line in file:
        # Remove whitespace/newline characters
        word = line.strip()

        # Construct the full URL to check (e.g., http://IP/admin)
        url = f"{target_url}/{word}"

        try:
            # Send a GET request with a 3‑second timeout
            response = requests.get(url, timeout=3)

            # If the response status code indicates something exists
            if response.status_code in [200, 301, 302, 403]:
                print(f"Found {url}. Status code: {response.status_code}")

        # If the script cannot connect to the server
        except requests.ConnectionError:
            print(f"[-] Failed to connect to: {url}")

        # If the request takes too long
        except requests.exceptions.ReadTimeout:
            print(f"[!] Timeout: {url}")