# -*- coding: utf-8 -*-
"""Vulert_Scrape.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18oaWG-mcmYU0KV0I5QqvY3bRXaXk5EbD
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL
base_url = "https://vulert.com/vuln-db/search?q=django&page="

# List to store all rows from each page
data = []

# Loop over pages
for page in range(1, 32):  # From page 1 to 31
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
df.to_csv("django_vulnerabilities.csv", index=False)
print("Data saved to django_vulnerabilities.csv")