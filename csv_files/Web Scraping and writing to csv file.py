# -*- coding: utf-8 -*-
#Script to scrape results from webpage and write in csv file, specifically flipkart search results.
#Note: The HTML Elements might change over time as the webpage changes. Use Inspect Element to figure out the correct elements and change for correct results.
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://www.flipkart.com/search?q=samsung%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", { "class": "_3pLy-c row"})
container = containers[0]
price = container.findAll("div", {"class": "_30jeq3 _1_WHN1"})
ratings = container.findAll("div", {"class": "_3LWZlK"})
filename = "F:/Python Projects/products.csv"
f = open(filename, "w")
headers = "Product_Name, Pricing, Ratings \n"
f.write(headers)
for container in containers:
    product = container.findAll("div", {"class": "_4rR01T"})
    product_name = product[0].text.strip()
    price_container = container.findAll("div", {"class": "_30jeq3 _1_WHN1"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "_3LWZlK"})
    rating = rating_container[0].text
    #print("Product_Name:"+ product_name)
    #print("Price: " + price)
    #print("Ratings:" + rating)
    edit_price = ''.join(price.split(','))  
    sym_rupee = edit_price.split("₹")  
    add_rs_price = "Rs"+sym_rupee[1]
    split_price = add_rs_price.split("E")
    final_price = split_price[0]  
  
    split_rating = str(rating).split(" ")  
    final_rating = split_rating[0]  
  
    print(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")  
    f.write(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")  
  
f.close()  