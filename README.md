# Extract Phones Data from MobileMasr Website

## Overview
This Python script performs **web scraping** to collect pricing data for **used smartphones** from MobileMasr platform.  
It extracts details such as product name, price, Type (new/used), seller name, and seller profile link,
and stores the results in a CSV file for further analytics or dashboard creation.

---

## How to Run the Script

1. **Install required libraries**
   pip install requests beautifulsoup4 csv timer

2. **Run the script**
   python WebScraping.py

3. **After running a file named**
   products.csv

---

## Output Fields
### Each row in the generated CSV file contains the following fields:
| Column        | Description                 |
| ------------- | --------------------------- |
| `Product`     | Phone name                  |
| `Price`       | Price of the phone          |
| `Type`        | Condition (New / Used)      |
| `Seller`      | Seller or store name        |
| `Seller_Link` | URL to the seller’s profile |
