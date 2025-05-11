
import requests
from bs4 import BeautifulSoup
import csv

# URL for OLX search results for "car cover"
url = "https://www.olx.in/items/q-car-cover"

# Set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send request and parse response
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Extract listings - OLX may use dynamic JS, so we try generic structure
items = soup.find_all("li", class_="EIR5N")

results = []

for item in items:
    title = item.find("span", class_="_2tW1I").text.strip() if item.find("span", class_="_2tW1I") else "N/A"
    price = item.find("span", class_="_89yzn").text.strip() if item.find("span", class_="_89yzn") else "N/A"
    location = item.find("span", class_="_2TVI3").text.strip() if item.find("span", class_="_2TVI3") else "N/A"
    link_tag = item.find("a")
    link = "https://www.olx.in" + link_tag['href'] if link_tag and 'href' in link_tag.attrs else "N/A"
    results.append([title, price, location, link])

# Save to CSV
with open("olx_car_cover_results.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location", "Link"])
    writer.writerows(results)

print("Scraped data saved to olx_car_cover_results.csv")
