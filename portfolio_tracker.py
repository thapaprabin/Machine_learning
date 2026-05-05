import requests
from bs4 import BeautifulSoup

class Stock:
    def __init__(self, symbol, quantity, buy_price):
        self.symbol = symbol.upper()
        self.quantity = quantity
        self.buy_price = buy_price
        self.current_price = 0.0

    def calculate_investment(self):
        """Calculates the total cost of buying this stock."""
        return self.quantity * self.buy_price

    def get_live_price(self):
        """Fetches the LTP from Merolagani."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        url = f"https://merolagani.com/CompanyDetail.aspx?symbol={self.symbol}"
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                return 0.0

            soup = BeautifulSoup(response.text, 'html.parser')
            
            # --- ROBUST SELECTOR LOGIC ---
            # Instead of a long ID, we find the table row that says 'Market Price'
            # and get the value next to it (the <td> tag).
            price_label = soup.find('th', string=lambda t: t and 'Market Price' in t)
            if price_label:
                price_text = price_label.find_next_sibling('td').text.strip()
                # Clean the data: remove commas (e.g., '1,200.50' -> '1200.50')
                self.current_price = float(price_text.replace(",", ""))
                return self.current_price
            
            return 0.0
        except Exception as e:
            print(f"Error fetching {self.symbol}: {e}")
            return 0.0

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def display_report(self):
        print(f"\n{'='*55}")
        print(f"{'NEPSE REAL-TIME PORTFOLIO TRACKER':^55}")
        print(f"{'='*55}")
        print(f"{'Symbol':<10} {'Qty':<8} {'Buy':<10} {'LTP':<10} {'P/L':<12}")
        print("-" * 55)
        
        total_inv = 0
        total_val = 0

        for stock in self.stocks:
            ltp = stock.get_live_price()
            investment = stock.calculate_investment()
            current_value = stock.quantity * ltp
            pl = current_value - investment
            
            total_inv += investment
            total_val += current_value

            # Displaying data with 2 decimal formatting
            print(f"{stock.symbol:<10} {stock.quantity:<8} {stock.buy_price:<10.2f} {ltp:<10.2f} {pl:<12.2f}")

        overall_pl = total_val - total_inv
        print("-" * 55)
        print(f"Total Investment: Rs. {total_inv:,.2f}")
        print(f"Portfolio Value:  Rs. {total_val:,.2f}")
        print(f"Overall Profit:   Rs. {overall_pl:,.2f}")
        print(f"{'='*55}")

if __name__ == "__main__":
    my_portfolio = Portfolio()

    # Logic: Add real NEPSE symbols
    #my_portfolio.add_stock(Stock("NICA", 50, 480))
    #my_portfolio.add_stock(Stock("HDL", 10, 2150))
    #my_portfolio.add_stock(Stock("UPPER", 100, 145))
    my_portfolio.add_stock(Stock("SMHL",100,525))

    my_portfolio.display_report()