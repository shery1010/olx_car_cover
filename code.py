
import requests
from bs4 import BeautifulSoup
import csv

# URL for "Car Cover" search on OLX
url = "https://www.olx.in/items/q-car-cover"

# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Open CSV file to write the results
with open("olx_car_covers.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location", "Link"])

    # Find listings on the page
    for item in soup.select('li.EIR5N'):
        title = item.select_one('span._2tW1I') or item.select_one('span._2poNJ')
        price = item.select_one('span._89yzn')
        location = item.select_one('span._2FcW-')
        link_tag = item.find('a')

        writer.writerow([
            title.text.strip() if title else "N/A",
            price.text.strip() if price else "N/A",
            location.text.strip() if location else "N/A",
            f"https://www.olx.in{link_tag['href']}" if link_tag else "N/A"
        ])

print("Scraping completed. Data saved to 'olx_car_covers.csv'.")
