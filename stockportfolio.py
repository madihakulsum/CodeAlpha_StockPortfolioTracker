stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print(" Welcome to the Stock Tracker!")
print("Available stocks:", ', '.join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not available.")
        continue
    try:
        quantity = int(input(f"How many shares of {stock}? "))
        if quantity <= 0:
            print("Quantity must be a positive number.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += stock_prices[stock] * quantity

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${qty * stock_prices[stock]}")

print(f"\nTotal Investment: ${total_investment}")

if input("\nSave to file? (yes/no): ").lower() == 'yes':
    with open("portfolio_summary.txt", "w") as f:
        f.write("Your Portfolio:\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
        f.write(f"\nTotal Investment: ${total_investment}")
    print("Saved to portfolio_summary.txt")