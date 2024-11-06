import csv
import requests

url = "https://amazon-web-scraping-api.p.rapidapi.com/products/search"

querystring = {"criteria":"pull up bar","page":"1","countryCode":"US","languageCode":"EN"}

headers = {
    "X-RapidAPI-Key": "72a341395bmsh2e5269750798dd4p19ed89jsne851274a515e",
    "X-RapidAPI-Host": "amazon-web-scraping-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

with open("pull_up_bar.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "Rating", "Reviews"])
    for item in data["products"]:
        name = item["name"]
        price = item["price"]["currentPrice"]
        rating = item["rating"]
        reviews = item["totalReviews"]
        writer.writerow([name, price, rating, reviews])
