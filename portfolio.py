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


# Main loop
while True:

    # Ask for stock name
    stock_name = input("\nEnter stock name: ").upper()

    # Stop the program
    if stock_name == "DONE":
        break

    # Check if stock exists
    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue
