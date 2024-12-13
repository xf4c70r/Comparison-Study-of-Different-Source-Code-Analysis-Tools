import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL
base_url = "https://vulert.com/vuln-db/search?q=fastapi&page="

# List to store all rows from each page
data = []

# Loop over pages
for page in range(0, 1):  # From page 1 to 31
    url = f"{base_url}{page}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the table (modify based on actual table structure if needed)
        table = soup.find("table")  # Assuming the table is the first/only one on the page
        if table:
            headers = [header.text.strip() for header in table.find_all("th")]
            rows = table.find_all("tr")[1:]  # Skip header row

            # Extract data from each row
            for row in rows:
                cells = [cell.text.strip() for cell in row.find_all("td")]
                if cells:
                    data.append(cells)

        print(f"Page {page} scraped successfully.")
    else:
        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")

    time.sleep(1)  # Pause to avoid overloading the server

# Save data to a DataFrame
df = pd.DataFrame(data, columns=headers)

# Save to a CSV file
df.to_csv("fastapi_vulnerabilities.csv", index=False)
print("Data saved to fastapi_vulnerabilities.csv")