''' python -m pip install request 
get data from web in hte form of html json or xml
python -m pip install beautifulsoup4 
parse html
'''
#from the bookstore website we will search for the data we need only 
#we need status code as 200.after that we can continue


import requests 
from bs4 import BeautifulSoup

url="https://books.toscrape.com/"
def scrape_books(url):
    response=requests.get(url)
    if response.status_code!=200:
        return
    #setting output to handle special characters
    response.encoding=response.apparent_encoding
    soup=BeautifulSoup(response.text,"html.parser")
    books=soup.find_all("article",class_="product_pod")
    #print(books)
    books_info=[]
    for book in books:
        title=book.h3.a['title']
        print(title)
        price_text=book.find("p",class_='price_color').text
        print(price_text)
        currency=price_text[0]
        price=float(price_text[1:])
        book_data={
            "title":title,
            "price":price,
            "currency":currency
        }
        books_info.append(book_data)
    
    return books_info

all_books=scrape_books(url)
with open("books.json","w") as f:
    import json
    json.dump(all_books,f,indent=4)
