# 📈 Stock Portfolio Tracker - CodeAlpha Internship Project

# Hardcoded stock prices (in INR)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 140,
    "INFY": 1500
}

def calculate_investment():
    total_value = 0
    user_portfolio = {}

    print("💼 Welcome to the Stock Portfolio Tracker!")
    print("Here are the available stocks and their prices (per share):\n")

    # Display available stocks
    for stock, price in stock_prices.items():
        print(f"📊 {stock} : ₹{price}")

    print("\n📝 Enter the stock symbol and quantity you want to buy.")
    print("🔚 Type 'done' when finished.\n")

    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not available. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            user_portfolio[stock] = user_portfolio.get(stock, 0) + quantity
        except ValueError:
            print("⚠️ Please enter a valid number.")

    # Display and save results
    print("\n📄 Investment Summary:")
    with open("portfolio_summary.txt", "w") as file:
        file.write("📄 Stock Portfolio Summary - CodeAlpha Internship\n\n")
        for stock, qty in user_portfolio.items():
            stock_value = stock_prices[stock] * qty
            total_value += stock_value
            summary_line = f"{stock} → {qty} shares × ₹{stock_prices[stock]} = ₹{stock_value}"
            print(summary_line)
            file.write(summary_line + "\n")
        print(f"\n💰 Total Investment Value: ₹{total_value}")
        file.write(f"\n💰 Total Investment Value: ₹{total_value}")

    print("\n✅ Summary saved to 'portfolio_summary.txt'.")

# Run the tracker
if __name__ == "__main__":
    calculate_investment()
