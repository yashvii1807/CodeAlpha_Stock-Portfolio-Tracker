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

 # Ask for quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue
# Get stock price
    price = stock_prices[stock_name]

    # Calculate investment
    investment = price * quantity

    # Add to total investment
    total_investment += investment

    # Store portfolio information
    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print("Investment for", stock_name, ":", "$" + str(investment))


# Display portfolio
print("\n====================================")
print("          YOUR PORTFOLIO")
print("====================================")

if len(portfolio) == 0:
    print("No stocks were added.")

else:
    for item in portfolio:
        print("\nStock:", item["stock"])
        print("Quantity:", item["quantity"])
        print("Price per share: $", item["price"])
        print("Investment: $", item["investment"])

    print("\n------------------------------------")
    print("Total Investment: $", total_investment)
    print("------------------------------------")


# Save result to a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("========================\n\n")

    for item in portfolio:
        file.write("Stock: " + item["stock"] + "\n")
        file.write("Quantity: " + str(item["quantity"]) + "\n")
        file.write("Price: $" + str(item["price"]) + "\n")
        file.write("Investment: $" + str(item["investment"]) + "\n")
        file.write("------------------------\n")

    file.write("\nTotal Investment: $" + str(total_investment))

print("\nPortfolio saved successfully to portfolio.txt")