#DEVELOPING A SIMPLE PROJECT 
'''
=====ABOUT THE PROJET===
PROBLEM:CALCULATING PROFIT IN THE STOCK INVESTED IN NEPSE
::THIS PROGRAM HELPS TO CALCULATE THE PROFIT/LOSS
AS PER THE CALCULATION OF VALUE OF THE STOCK AS THE LTP.
MULTIPLE STOCKS CAN BE CALCULATED AT ONCE.''' 

import requests #(request) is library to make web request 
from bs4 import BeautifulSoup #for web scraping 
class Stock:
    def __init__(self,symbol,quantity,buy_price):
        self.symbol=symbol.upper()
        self.quantity=quantity
        self.buy_price=buy_price
        self.current_price=0
        #we declare a function that calculate his investment in stock
    def investment(self): #before investment was inside the init funciton so calling outside class had a problem.Solved:Indentation fixed
            return self.quantity*self.buy_price
    def latest_price(self):
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        } #from deepseek:headers mimic real browser(without headers some websites return error pages or block request)
        url=f"https://merolagani.com/CompanyDetail.aspx?symbol={self.symbol}"
        try:
            response=requests.get(url,headers=headers,timeout=10) #fixed | 's' request-> requests |
            if response.status_code !=200:
                print("Server Error.")
                return
            soup=BeautifulSoup(response.text,'html.parser')
            price=soup.find('th',string=lambda t:t and 'Market Price' in t)
            #so here:
            #we find heading as market price,lambda is used for flexibility.for eg:market price and MARKET price
            if price:
                price_text=price.find_next_sibling('td').text.strip() 
                #strip removes any kind of characters like whitespaces
                #cleaning comma and converting to float for easy calc.
                self.current_price=float(price_text.replace(",","")) #we replace comma with empty value
                return self.current_price
            else:
                print("Could not fetch the data")
                return
        except Exception as e:
            print(f"ERROR CONNECTING {e}") 
            return
#Now another class for information about portfolio.
class Portfolio:
    def __init__(self):
        self.stocks=[]#list to store stock names 
    def add_stock(self,stock):
        self.stocks.append(stock)
    def display(self):
        print("+ + + Nepse portfolio + + +")
        print("=" * 50)
        print(f"{'SYMBOL':<10}{'Quantity':<10}{'WACC':<10}{'LTP':<10}{'P/L':<10} ")
        print("=" * 50)

        #initially the value is 0
        total_inv=0
        total_value=0

        #now we calculate the value of every stock using for loop as per ltp.
        for stock in self.stocks:
            ltp=stock.latest_price()
            investment=stock.investment()
            current_value=stock.quantity*ltp
            pl=current_value-investment
            total_inv += investment
            total_value += current_value
            print(f"{stock.symbol:<10}{stock.quantity:<10}{stock.buy_price:<10}{ltp:<10}{pl:<10}")
        overall_pl=total_value-total_inv
        print(f"Total Investment: Rs. {total_inv:.2f}")
        print(f"Portfolio Value:  Rs. {total_value:.2f}")
        print(f"Overall Profit:   Rs. {overall_pl:.2f}") 
if __name__=="__main__":
    my_portfolio=Portfolio()#portfolio is a class my portfolio is an object
    my_portfolio.add_stock(Stock("SMHL",100,300))
    my_portfolio.display()

#ERROR OCCURED WHILE DOING THIS PROGRAM

 #1.indentation 
 #2.syntax