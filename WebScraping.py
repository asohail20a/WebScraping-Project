# Import Libraries:
import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse
import time

Product_Details = []
base_url = "https://mobilemasr.com"


def PageInfo():
    for page in range(1, 24):

        PageLink = f"https://mobilemasr.com/category/%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84/products?page={page}"
        HomePage = requests.get(PageLink)
        Soup = BeautifulSoup(HomePage.text, "html.parser")
        Products = Soup.find_all(
            "div",
            {
                "class": "product-card max-w-sm bg-white rounded-lg relative font-noto-or-Trebuchet h-[409px] group w-[140px] sm:w-[180px] md:w-[200px] my-2"
            },
        )

        for i in Products:

            Type = i.find("span").text  # جديد ولا مستعمل
            Seller = i.find("p").text
            Seller_tag = i.find(
                "a", {"class": "flex items-center space-x-2 py-1 rounded"}
            )
            Seller_URL = Seller_tag.get("href") if Seller_tag else None
            Seller_URL = urllib.parse.urljoin(base_url, Seller_URL)
            Price = i.find("span", {"class": "text-sm"}).text
            Product_Name = i.find(
                "p",
                {
                    "class": "h-[47px] font-semibold leading-[1.2rem] text-gray-800 text-[12px] md:text-[13px]"
                },
            ).text

            Product_Details.append(
                {
                    "ProductName": Product_Name,
                    "Type": Type,
                    "Seller": Seller,
                    "Price": Price,
                    "CompanyURL": Seller_URL,
                }
            )
    time.sleep(3)


def loading_to_csv():
    header = Product_Details[0].keys()
    with open("D:/products.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(Product_Details)
        print("Congratulations ✅")


PageInfo()
loading_to_csv()
