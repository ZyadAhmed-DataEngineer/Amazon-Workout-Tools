import csv
import requests

url = "https://amazon-web-scraping-api.p.rapidapi.com/products/search"

headers = {
    "X-RapidAPI-Key": "98de7e6d1bmsh37dd9ec9c9f6ed0p1db168jsn44120b8d5b28",
    "X-RapidAPI-Host": "amazon-web-scraping-api.p.rapidapi.com",
}

with open("push_up_bar.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "Rating", "Reviews"])  # Write header row

    for page in range(10):  # Request first 10 pages
        querystring = {
            "criteria": "push up bar",
            "countryCode": "US",
            "languageCode": "EN",
            "pageSize": "50000",
        }

        response = requests.get(url, headers=headers, params=querystring)
        try:
            data = response.json()
        except ValueError:
            print(f"Error parsing JSON on page {page}")
            continue

        if not data:
            break

        for product in data["products"]:
            name = product.get("name")
            price = product.get("price", {}).get("currentPrice")
            rating = product.get("rating")
            reviews = product.get("totalReviews")
            writer.writerow([name, price, rating, reviews])
