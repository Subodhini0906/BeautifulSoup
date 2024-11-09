import os
import requests

def fetchAndSavetoFile(url, path):
    try:
        # Send GET request to the URL
        r = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if r.status_code == 200:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
            # Write the content to the file
            with open(path, "w", encoding="utf-8") as f:
                f.write(r.text)
            print(f"Data successfully saved to {path}")
        else:
            print(f"Failed to retrieve the URL. Status code: {r.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# URL to fetch
url = "https://timesofindia.indiatimes.com/world/pakistan/blast-at-pakistan-railway-station-kills-over-a-dozen-injures-30/articleshow/115104101.cms"

# Path where the file will be saved
file_path = "data/times.html"

# Call the function to fetch and save the data
fetchAndSavetoFile(url, file_path)
