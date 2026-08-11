# CodeAlpha Task 2
# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

# Store user's portfolio
portfolio = []

# Store total investment
total_investment = 0

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$" + str(price))

print("\nEnter 'DONE' when you finish adding stocks.")
